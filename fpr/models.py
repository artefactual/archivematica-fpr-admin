"""
:mod:`fpr.models` 

Describes the data model for the FPR

"""
import logging
import uuid

from django.db import models

from annoying.functions import get_object_or_None
from autoslug import AutoSlugField
from django_extensions.db.fields import UUIDField

from django.db.models import Q, Model
from django.core.validators import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS

logger = logging.getLogger(__name__)

############################### API V2 MODELS ###############################

############ MANAGERS ############

class Enabled(models.Manager):
    """ Manager to only return enabled objects.

    Filters by enabled=True.  """
    def get_query_set(self):
        return super(Enabled, self).get_query_set().filter(enabled=True)

class NormalizationRules(models.Manager):
    """ Manager to only return normalization FPCommands.  """
    def get_query_set(self):
        return super(NormalizationRules, self).get_query_set().filter(enabled=True)


############ MIXINS ############

class VersionedModel(models.Model):
    replaces = models.ForeignKey('self', to_field='uuid', null=True, blank=True)
    enabled = models.BooleanField(default=True)

    def save(self, replacing=None, *args, **kwargs):
        if replacing:
            self.replaces = replacing
            # Force it to create a new row
            self.uuid = None
            self.pk = None
            self.enabled = True # in case the version was created using an older version
            replacing.enabled = False
            replacing.save()
        super(VersionedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

    objects = models.Manager()
    active = Enabled()
    normalization = NormalizationRules()

############ FORMATS ############

class Format(models.Model):
    """ User-friendly description of format.

    Collects multiple related FormatVersions to one conceptual version.

    Eg. GIF, Word file."""
    uuid = UUIDField(editable=False, unique=True, version=4, help_text="Unique identifier")
    description = models.CharField(max_length=128, help_text="Common name of format")
    group = models.ForeignKey('FormatGroup', to_field='uuid')
    slug = AutoSlugField(populate_from='description')

    class Meta:
        verbose_name = "Format"
        ordering = ['group']

    def __unicode__(self):
        return u"{}: {}".format(self.group.description, self.description)


class FormatGroup(models.Model):
    """ Group/classification for formats.  Eg. image, video, audio. """
    uuid = UUIDField(editable=False, unique=True, version=4, help_text="Unique identifier")
    description = models.CharField(max_length=128, verbose_name='Format Group')
    slug = AutoSlugField(populate_from='description')

    class Meta:
        verbose_name = "Format Group"

    def __unicode__(self):
        return u"{}".format(self.description)


class FormatVersion(VersionedModel, models.Model):
    """ Format that a tool identifies. """
    uuid = UUIDField(editable=False, unique=True, version=4, help_text="Unique identifier")
    format = models.ForeignKey('Format', to_field='uuid', related_name='version_set')
    version = models.CharField(max_length=10, null=True, blank=True)
    pronom_id = models.CharField(max_length=16, blank=True)
    description = models.CharField(max_length=128, null=True, blank=True,
        help_text='Formal name to go in the METS file.')
    access_format = models.BooleanField(default=False)
    preservation_format = models.BooleanField(default=False)

    lastmodified = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='description', unique_with='format', always_update=True)

    class Meta:
        verbose_name = "Format Version"
        ordering = ['format', 'description']
      
    def validate_unique(self, *args, **kwargs):
        super(FormatVersion, self).validate_unique(*args, **kwargs)

        if len(self.pronom_id) > 0:
            qs = self.__class__._default_manager.filter(
                pronom_id=self.pronom_id,
                enabled=1
            )

            if not self._state.adding and self.pk is not None:
                qs = qs.exclude(pk=self.pk)

            if qs.exists():
                raise ValidationError( {
                        NON_FIELD_ERRORS:('Unable to save, an active Format Version  with this pronom id already exists.',)})

 
    def __unicode__(self):
        return u"{}: {}".format(self.format, self.description)


############ ID TOOLS ############

class IDCommand(VersionedModel, models.Model):
    """ Command to run an IDToolConfig and parse the output.

    IDCommand runs 'script' (which runs an IDTool with a specific IDToolConfig)
    and parses the output. """
    uuid = UUIDField(editable=False, unique=True, version=4, help_text="Unique identifier")
    description = models.CharField(max_length=256, verbose_name='Identifier', help_text="Name to identify script")
    script = models.TextField(help_text="Script to be executed.")
    SCRIPT_TYPE_CHOICES = (
        ('bashScript', 'Bash Script'),
        ('pythonScript', 'Python Script'),
        ('command', 'Command Line'),
        ('as_is', 'No shebang (#!/path/to/interpreter) needed')
    )
    script_type = models.CharField(max_length=16, choices=SCRIPT_TYPE_CHOICES)
    tool = models.ManyToManyField('IDTool', through='IDToolConfig', related_name='command', null=True, blank=True)
    lastmodified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Format Identification Command"

    def __unicode__(self):
        return u"{}".format(self.description)


class IDRule(VersionedModel, models.Model):
    """ Mapping between an IDCommand output and a FormatVersion. """
    uuid = UUIDField(editable=False, unique=True, version=4, help_text="Unique identifier")
    command = models.ForeignKey('IDCommand', to_field='uuid')
    format = models.ForeignKey('FormatVersion', to_field='uuid')
    # Output from IDToolConfig.command to match on that gives the format
    command_output = models.TextField()

    lastmodified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Format Identification Rule"

    def validate_unique(self, *args, **kwargs):
        super(IDRule, self).validate_unique(*args, **kwargs)

        qs = self.__class__._default_manager.filter(
            command=self.command,
            command_output=self.command_output,
            enabled=1
        )

        if not self._state.adding and self.pk is not None:
            qs = qs.exclude(pk=self.pk)

        if qs.exists():
            raise ValidationError( {
                    NON_FIELD_ERRORS:('Unable to save, a rule with this output already exists for this command.',)})

    def __unicode__(self):
        return u"{command} with {output} is {format}".format(command=self.command,
            output=self.command_output,
            format=self.format)


class IDTool(models.Model):
    """ Tool used to identify formats.  Eg. DROID """
    uuid = UUIDField(editable=False, unique=True, version=4, help_text="Unique identifier")
    description = models.CharField(max_length=256, help_text="Name of tool")
    version = models.CharField(max_length=64)
    enabled = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='_slug', always_update=True)

    class Meta:
        verbose_name = "Format Identification Tool"

    objects = models.Manager()
    active = Enabled()

    def __unicode__(self):
        return u"{} version {}".format(self.description, self.version)

    def _slug(self):
        """ Returns string to be slugified. """
        return "{} {}".format(self.description, self.version)


class IDToolConfig(VersionedModel, models.Model):
    """ Tool and configuration used to identify formats.

    Eg. DROID mime-type, DROID PUID, Jhove format. """
    uuid = UUIDField(editable=False, unique=True, version=4, help_text="Unique identifier")
    tool = models.ForeignKey('IDTool', to_field='uuid', related_name='config_set')
    CONFIG_CHOICES = (
        ('PUID', 'PUID'),
        ('MIME', 'mime-type'),
        ('ext', 'file extension')
    )
    config = models.CharField(max_length=4, choices=CONFIG_CHOICES)
    command = models.ForeignKey('IDCommand', to_field='uuid')

    lastmodified = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='config', unique_with='tool')

    class Meta:
        verbose_name = "Format Identification Tool Configuration"

    def __unicode__(self):
        return u"{tool} {config} runs {command}".format(tool=self.tool, 
            config=self.get_config_display(),
            command=self.command)

    def save(self, *args, **kwargs):
        super(IDToolConfig, self).save(*args, **kwargs)
        # If part of archivematica, create user choice replacement dict
        try:
            from main.models import MicroServiceChoiceReplacementDic
        except ImportError:
            return
        # Remove existing object
        MicroServiceChoiceReplacementDic.objects.filter(replacementdic__contains=self.uuid).delete()
        if self.enabled:
            # Add replacement to MicroServiceChoiceReplacementDic
            at_link_transfer = 'f09847c2-ee51-429a-9478-a860477f6b8d'
            at_link_ingest = '7a024896-c4f7-4808-a240-44c87c762bc5'
            # {"%IDCommand%": self.command.uuid}
            replace = '{{"%IDCommand%":"{0}"}}'.format(self.uuid)
            MicroServiceChoiceReplacementDic.objects.create(
                id=str(uuid.uuid4()),
                choiceavailableatlink=at_link_transfer,
                description=str(self),
                replacementdic=replace,
            )
            MicroServiceChoiceReplacementDic.objects.create(
                id=str(uuid.uuid4()),
                choiceavailableatlink=at_link_ingest,
                description=str(self),
                replacementdic=replace,
            )


############ NORMALIZATION ############

class FPRule(VersionedModel, models.Model):
    uuid = UUIDField(editable=False, unique=True, version=4, help_text="Unique identifier")
    PURPOSE_CHOICES = (
        ('access', 'Access'),
        ('preservation', 'Preservation'),
        ('thumbnail', 'Thumbnail'),
        ('extract', 'Extract'),
    )
    purpose = models.CharField(max_length=16, choices=PURPOSE_CHOICES)
    command = models.ForeignKey('FPCommand', to_field='uuid')
    format = models.ForeignKey('FormatVersion', to_field='uuid')

    count_attempts = models.IntegerField(default=0)
    count_okay = models.IntegerField(default=0)
    count_not_okay = models.IntegerField(default=0)

    lastmodified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Format Policy Rule"

    def __unicode__(self):
        return u"Normalize {format} for {purpose} via {command}".format(
            format=self.format,
            purpose=self.get_purpose_display(),
            command=self.command)

    def save(self, *args, **kwargs):
        super(FPRule, self).save(*args, **kwargs)
        # TODO this might need to be moved/updated elsewhere
        # If part of Archivematica, update chain link and task config
        try:
            from main.models import MicroServiceChainLink, MicroServiceChainLinkExitCode, TaskConfig
        except ImportError:
            pass
        else:
            if self.enabled:
                # Create new TaskConfig
                transcode_task_type='5e70152a-9c5b-4c17-b823-c9298c546eeb'
                task_config = TaskConfig.objects.create(
                    id=str(uuid.uuid4()),
                    tasktype=transcode_task_type,
                    tasktypepkreference=self.uuid,
                    description=unicode(self)
                )
                # Create new MicroServiceChainLink
                # defaultnextchainlink should point at the default action for
                # that purpose, in case the FPRule fails.
                # TODO need to set up default rules for FPR v2 API
                if self.purpose == 'access':
                    defaultnextchainlink='006f6fc3-5837-4333-8920-fefc977e7a76'
                elif self.purpose == 'thumbnail':
                    defaultnextchainlink='a7fe8db6-387c-4295-b488-56e1b55c57d9'
                else:
                    defaultnextchainlink=None
                mscl = MicroServiceChainLink.objects.create(
                    id=str(uuid.uuid4()),
                    currenttask=task_config.id,
                    defaultnextchainlink=defaultnextchainlink,
                    defaultplaysound=None,
                    microservicegroup="Normalize",
                )
                # Create new MicroServiceChainLinkExitCode
                MicroServiceChainLinkExitCode.objects.create(
                    id=str(uuid.uuid4()),
                    microservicechainlink=mscl.id,
                    exitcode=0,  # default
                    nextmicroservicechainlink=None,  # default
                )


class FPCommand(VersionedModel, models.Model):
    uuid = UUIDField(editable=False, unique=True, version=4, help_text="Unique identifier")
    # ManyToManyField may not be the best choice here
    tool = models.ManyToManyField('FPTool', related_name="commands", through='FPCommandTool')
    description = models.CharField(max_length=256)
    command = models.TextField()
    SCRIPT_TYPE_CHOICES = (
        ('bashScript', 'Bash Script'),
        ('pythonScript', 'Python Script'),
        ('command', 'Command Line'),
        ('as_is', 'No shebang (#!/path/to/interpreter) needed')
    )
    script_type = models.CharField(max_length=16, choices=SCRIPT_TYPE_CHOICES)
    output_location = models.TextField(null=True, blank=True)
    output_format = models.ForeignKey('FormatVersion', to_field='uuid', )
    COMMAND_USAGE_CHOICES = (
        ('normalization', 'Normalization'),
        ('event_detail', 'Event Detail'),
        ('verification', 'Verification'),
    )
    command_usage = models.CharField(max_length=16, choices=COMMAND_USAGE_CHOICES)
    verification_command = models.ForeignKey('self', to_field='uuid', null=True, blank=True, related_name='+')
    event_detail_command = models.ForeignKey('self', to_field='uuid', null=True, blank=True, related_name='+')

    lastmodified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Format Policy Command"

    def __unicode__(self):
        return u"{}".format(self.description)


class FPTool(models.Model):
    """ Tool used to perform normalization.  Eg. convert, ffmpeg, ps2pdf. """
    uuid = UUIDField(editable=False, unique=True, version=4, help_text="Unique identifier")
    description = models.CharField(max_length=256, help_text="Name of tool")
    version = models.CharField(max_length=64)
    enabled = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='_slug')
    # Many to many field is on FPCommand

    class Meta:
        verbose_name = "Normalization Tool"

    def __unicode__(self):
        return u"{} version {}".format(self.description, self.version)

    def _slug(self):
        """ Returns string to be slugified. """
        return "{} {}".format(self.description, self.version)


class FPCommandTool(models.Model):
    """ Many-to-many relationship between FPcommand and FPTool. """
    # Needs to set to_field='uuid' which cannot be done with M2M field
    uuid = UUIDField(editable=False, unique=True, version=4, help_text="Unique identifier")
    command = models.ForeignKey('FPCommand', to_field='uuid')
    tool = models.ForeignKey('FPTool', to_field='uuid')


############################### API V1 MODELS ###############################

class Agent(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, db_column='uuid')
    agentIdentifierType = models.CharField(max_length=100)
    agentIdentifierValue = models.CharField(max_length=100)
    agentName = models.CharField(max_length=100)
    agentType = models.CharField(max_length=100)
    clientIP = models.CharField(max_length=100)
    class Meta:
        db_table=u'Agent'

class CommandType(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, db_column='pk')
    replaces = models.CharField(null=True, max_length=50, db_column='replaces')
    type = models.TextField(db_column='type')
    lastmodified = models.DateTimeField(db_column='lastModified')
    enabled = models.IntegerField(null=True, db_column='enabled', default=1)
    class Meta:
        db_table = u'CommandType'

class Command(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, db_column='pk')
    #commandType = models.ForeignKey(CommandType, db_column='commandType')
    commandUsage = models.CharField(max_length=15)
    commandType = models.CharField(max_length=36)
    #verificationCommand = models.ForeignKey('self', null=True, related_name='+', db_column='verificationCommand')
    verificationCommand = models.CharField(max_length=36, null=True)
    #eventDetailCommand = models.ForeignKey('self', null=True, related_name='+', db_column='eventDetailCommand')
    eventDetailCommand = models.CharField(max_length=36, null=True)
    #supportedBy = models.ForeignKey('self', null=True, related_name='+', db_column='supportedBy')
    supportedBy = models.CharField(max_length=36, null=True, db_column='supportedBy')
    command = models.TextField(db_column='command')
    outputLocation = models.TextField(db_column='outputLocation', null=True)
    description = models.TextField(db_column='description')
    outputFileFormat = models.TextField(db_column='outputFileFormat', null=True)
    #replaces = models.ForeignKey('self', related_name='+', db_column='replaces', null=True)
    replaces = models.CharField(max_length=36, null=True, db_column='replaces')
    lastmodified = models.DateTimeField(db_column='lastModified', null=True)
    enabled = models.IntegerField(null=True, db_column='enabled', default=1)
    class Meta:
        db_table = u'Command'

class CommandsSupportedBy(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, db_column='pk')
    description = models.TextField(null=True, db_column='description')
    #replaces = models.ForeignKey(Command)
    replaces = models.CharField(max_length=36, null=True, db_column='replaces')
    lastmodified = models.DateTimeField(db_column='lastModified')
    enabled = models.IntegerField(null=True, db_column='enabled', default=1)
    class Meta:
        db_table = u'CommandsSupportedBy'

    def __unicode__(self):
        return u'{}'.format(self.description)

class FileIDType(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, db_column='pk')
    description = models.TextField(null=True, db_column='description')
    replaces = models.CharField(null=True, max_length=50, db_column='replaces')
    lastmodified = models.DateTimeField(db_column='lastModified')
    enabled = models.IntegerField(null=True, db_column='enabled', default=1)
    class Meta:
        db_table = u'FileIDType'

class FileID(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, db_column='pk')
    description = models.TextField(db_column='description')
    validpreservationformat = models.IntegerField(null=True, db_column='validPreservationFormat', default=0)
    validaccessformat = models.IntegerField(null=True, db_column='validAccessFormat', default=0)
    #fileidtype = models.ForeignKey(FileIDType, null=True, blank=True, default = None)
    fileidtype= models.CharField(max_length=36, null=True, db_column='fileidtype_id')
    replaces = models.CharField(null=True, max_length=36, db_column='replaces')
    lastmodified = models.DateTimeField(db_column='lastModified')
    enabled = models.IntegerField(null=True, db_column='enabled', default=1)

    # V2 API
    format = models.ForeignKey('FormatVersion', to_field='uuid', null=True)

    class Meta:
        db_table = u'FileID'

class CommandClassification(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, db_column='pk')
    classification = models.TextField(null=True, db_column='classification')
    replaces = models.CharField(null=True, max_length=50, db_column='replaces')
    lastmodified = models.DateTimeField(db_column='lastModified')
    enabled = models.IntegerField(null=True, db_column='enabled', default=1)
    class Meta:
        db_table = u'CommandClassification'

class CommandRelationship(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, db_column='pk')
    #commandClassification = models.ForeignKey(CommandClassification, db_column='commandClassification')
    commandClassification = models.CharField(max_length=36)
    #command = models.ForeignKey(Command, null=True, db_column='command')
    #fileID = models.ForeignKey(FileID, db_column='fileID')
    #replaces = models.CharField(null=True, max_length=50, db_column='replaces')
    command = models.CharField(max_length=36, null=True)
    fileID = models.CharField(max_length=36, null=True)
    replaces = models.CharField(max_length=36, null=True)
    lastmodified = models.DateTimeField(db_column='lastModified')
    enabled = models.IntegerField(null=True, db_column='enabled', default=1)
    class Meta:
        db_table = u'CommandRelationship'

class FileIDsBySingleID(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, db_column='pk')
    #fileID = models.ForeignKey(FileID, db_column='fileID')
    fileID = models.CharField(max_length=36, null=True)
    id = models.TextField(db_column='id')
    tool = models.TextField(db_column='tool')
    toolVersion = models.TextField(db_column='toolVersion', null=True)
    replaces = models.CharField(null=True, max_length=50, db_column='replaces')
    lastmodified = models.DateTimeField(db_column='lastModified')
    enabled = models.IntegerField(null=True, db_column='enabled', default=1)
    class Meta:
        db_table = u'FileIDsBySingleID'


