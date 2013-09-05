# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Format'
        db.create_table(u'fpr_format', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.FormatGroup'], to_field='uuid')),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='description')),
        ))
        db.send_create_signal(u'fpr', ['Format'])

        # Adding model 'FormatGroup'
        db.create_table(u'fpr_formatgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='description')),
        ))
        db.send_create_signal(u'fpr', ['FormatGroup'])

        # Adding model 'FormatVersion'
        db.create_table(u'fpr_formatversion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('format', self.gf('django.db.models.fields.related.ForeignKey')(related_name='version_set', to_field='uuid', to=orm['fpr.Format'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('access_format', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('preservation_format', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('replaces', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.FormatVersion'], null=True, blank=True)),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=('format',), max_length=50, populate_from='description')),
        ))
        db.send_create_signal(u'fpr', ['FormatVersion'])

        # Adding model 'IDCommand'
        db.create_table(u'fpr_idcommand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('script', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('replaces', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.IDCommand'], null=True, blank=True)),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'fpr', ['IDCommand'])

        # Adding model 'IDRule'
        db.create_table(u'fpr_idrule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('tool', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.IDCommand'], to_field='uuid')),
            ('format', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.FormatVersion'], to_field='uuid')),
            ('script_output', self.gf('django.db.models.fields.TextField')()),
            ('replaces', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.IDRule'], null=True, blank=True)),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'fpr', ['IDRule'])

        # Adding model 'IDTool'
        db.create_table(u'fpr_idtool', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='_slug')),
        ))
        db.send_create_signal(u'fpr', ['IDTool'])

        # Adding model 'IDToolConfig'
        db.create_table(u'fpr_idtoolconfig', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('tool', self.gf('django.db.models.fields.related.ForeignKey')(related_name='config_set', to_field='uuid', to=orm['fpr.IDTool'])),
            ('config', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('command', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.IDCommand'], to_field='uuid')),
            ('replaces', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.IDToolConfig'], null=True, blank=True)),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=('tool',), max_length=50, populate_from='config')),
        ))
        db.send_create_signal(u'fpr', ['IDToolConfig'])

        # Adding model 'FPRule'
        db.create_table(u'fpr_fprule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('command', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.NormalizationCommand'])),
            ('format', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.FormatVersion'])),
            ('replaces', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.FPRule'], null=True, blank=True)),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'fpr', ['FPRule'])

        # Adding model 'NormalizationCommand'
        db.create_table(u'fpr_normalizationcommand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('command', self.gf('django.db.models.fields.TextField')()),
            ('script_type', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('output_file_format', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('output_location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('command_usage', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('verification_command', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['fpr.NormalizationCommand'])),
            ('event_detail_command', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['fpr.NormalizationCommand'])),
            ('supported_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.CommandsSupportedBy'], null=True, blank=True)),
            ('replaces', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.NormalizationCommand'], null=True, blank=True)),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'fpr', ['NormalizationCommand'])

        # Adding M2M table for field tool on 'NormalizationCommand'
        db.create_table(u'fpr_normalizationcommand_tool', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('normalizationcommand', models.ForeignKey(orm[u'fpr.normalizationcommand'], null=False)),
            ('normalizationtool', models.ForeignKey(orm[u'fpr.normalizationtool'], null=False))
        ))
        db.create_unique(u'fpr_normalizationcommand_tool', ['normalizationcommand_id', 'normalizationtool_id'])

        # Adding model 'NormalizationTool'
        db.create_table(u'fpr_normalizationtool', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='_slug')),
        ))
        db.send_create_signal(u'fpr', ['NormalizationTool'])

        # Adding model 'Agent'
        db.create_table(u'Agent', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True, db_column='uuid')),
            ('agentIdentifierType', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('agentIdentifierValue', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('agentName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('agentType', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('clientIP', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'fpr', ['Agent'])

        # Adding model 'CommandType'
        db.create_table(u'CommandType', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True, db_column='pk')),
            ('replaces', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, db_column='replaces')),
            ('type', self.gf('django.db.models.fields.TextField')(db_column='type')),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(db_column='lastModified')),
            ('enabled', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, db_column='enabled')),
        ))
        db.send_create_signal(u'fpr', ['CommandType'])

        # Adding model 'Command'
        db.create_table(u'Command', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True, db_column='pk')),
            ('commandUsage', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('commandType', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('verificationCommand', self.gf('django.db.models.fields.CharField')(max_length=36, null=True)),
            ('eventDetailCommand', self.gf('django.db.models.fields.CharField')(max_length=36, null=True)),
            ('supportedBy', self.gf('django.db.models.fields.CharField')(max_length=36, null=True, db_column='supportedBy')),
            ('command', self.gf('django.db.models.fields.TextField')(db_column='command')),
            ('outputLocation', self.gf('django.db.models.fields.TextField')(null=True, db_column='outputLocation')),
            ('description', self.gf('django.db.models.fields.TextField')(db_column='description')),
            ('outputFileFormat', self.gf('django.db.models.fields.TextField')(null=True, db_column='outputFileFormat')),
            ('replaces', self.gf('django.db.models.fields.CharField')(max_length=36, null=True, db_column='replaces')),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column='lastModified')),
            ('enabled', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, db_column='enabled')),
        ))
        db.send_create_signal(u'fpr', ['Command'])

        # Adding model 'CommandsSupportedBy'
        db.create_table(u'CommandsSupportedBy', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True, db_column='pk')),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, db_column='description')),
            ('replaces', self.gf('django.db.models.fields.CharField')(max_length=36, null=True, db_column='replaces')),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(db_column='lastModified')),
            ('enabled', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, db_column='enabled')),
        ))
        db.send_create_signal(u'fpr', ['CommandsSupportedBy'])

        # Adding model 'FileIDType'
        db.create_table(u'FileIDType', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True, db_column='pk')),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, db_column='description')),
            ('replaces', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, db_column='replaces')),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(db_column='lastModified')),
            ('enabled', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, db_column='enabled')),
        ))
        db.send_create_signal(u'fpr', ['FileIDType'])

        # Adding model 'FileID'
        db.create_table(u'FileID', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True, db_column='pk')),
            ('description', self.gf('django.db.models.fields.TextField')(db_column='description')),
            ('validpreservationformat', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, db_column='validPreservationFormat')),
            ('validaccessformat', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, db_column='validAccessFormat')),
            ('fileidtype', self.gf('django.db.models.fields.CharField')(max_length=36, null=True, db_column='fileidtype_id')),
            ('replaces', self.gf('django.db.models.fields.CharField')(max_length=36, null=True, db_column='replaces')),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(db_column='lastModified')),
            ('enabled', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, db_column='enabled')),
            ('format', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fpr.FormatVersion'], to_field='uuid', null=True)),
        ))
        db.send_create_signal(u'fpr', ['FileID'])

        # Adding model 'CommandClassification'
        db.create_table(u'CommandClassification', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True, db_column='pk')),
            ('classification', self.gf('django.db.models.fields.TextField')(null=True, db_column='classification')),
            ('replaces', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, db_column='replaces')),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(db_column='lastModified')),
            ('enabled', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, db_column='enabled')),
        ))
        db.send_create_signal(u'fpr', ['CommandClassification'])

        # Adding model 'CommandRelationship'
        db.create_table(u'CommandRelationship', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True, db_column='pk')),
            ('commandClassification', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('command', self.gf('django.db.models.fields.CharField')(max_length=36, null=True)),
            ('fileID', self.gf('django.db.models.fields.CharField')(max_length=36, null=True)),
            ('replaces', self.gf('django.db.models.fields.CharField')(max_length=36, null=True)),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(db_column='lastModified')),
            ('enabled', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, db_column='enabled')),
        ))
        db.send_create_signal(u'fpr', ['CommandRelationship'])

        # Adding model 'FileIDsBySingleID'
        db.create_table(u'FileIDsBySingleID', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True, db_column='pk')),
            ('fileID', self.gf('django.db.models.fields.CharField')(max_length=36, null=True)),
            ('id', self.gf('django.db.models.fields.TextField')(db_column='id')),
            ('tool', self.gf('django.db.models.fields.TextField')(db_column='tool')),
            ('toolVersion', self.gf('django.db.models.fields.TextField')(null=True, db_column='toolVersion')),
            ('replaces', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, db_column='replaces')),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(db_column='lastModified')),
            ('enabled', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, db_column='enabled')),
        ))
        db.send_create_signal(u'fpr', ['FileIDsBySingleID'])


    def backwards(self, orm):
        # Deleting model 'Format'
        db.delete_table(u'fpr_format')

        # Deleting model 'FormatGroup'
        db.delete_table(u'fpr_formatgroup')

        # Deleting model 'FormatVersion'
        db.delete_table(u'fpr_formatversion')

        # Deleting model 'IDCommand'
        db.delete_table(u'fpr_idcommand')

        # Deleting model 'IDRule'
        db.delete_table(u'fpr_idrule')

        # Deleting model 'IDTool'
        db.delete_table(u'fpr_idtool')

        # Deleting model 'IDToolConfig'
        db.delete_table(u'fpr_idtoolconfig')

        # Deleting model 'FPRule'
        db.delete_table(u'fpr_fprule')

        # Deleting model 'NormalizationCommand'
        db.delete_table(u'fpr_normalizationcommand')

        # Removing M2M table for field tool on 'NormalizationCommand'
        db.delete_table('fpr_normalizationcommand_tool')

        # Deleting model 'NormalizationTool'
        db.delete_table(u'fpr_normalizationtool')

        # Deleting model 'Agent'
        db.delete_table(u'Agent')

        # Deleting model 'CommandType'
        db.delete_table(u'CommandType')

        # Deleting model 'Command'
        db.delete_table(u'Command')

        # Deleting model 'CommandsSupportedBy'
        db.delete_table(u'CommandsSupportedBy')

        # Deleting model 'FileIDType'
        db.delete_table(u'FileIDType')

        # Deleting model 'FileID'
        db.delete_table(u'FileID')

        # Deleting model 'CommandClassification'
        db.delete_table(u'CommandClassification')

        # Deleting model 'CommandRelationship'
        db.delete_table(u'CommandRelationship')

        # Deleting model 'FileIDsBySingleID'
        db.delete_table(u'FileIDsBySingleID')


    models = {
        u'fpr.agent': {
            'Meta': {'object_name': 'Agent', 'db_table': "u'Agent'"},
            'agentIdentifierType': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'agentIdentifierValue': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'agentName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'agentType': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'clientIP': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True', 'db_column': "'uuid'"})
        },
        u'fpr.command': {
            'Meta': {'object_name': 'Command', 'db_table': "u'Command'"},
            'command': ('django.db.models.fields.TextField', [], {'db_column': "'command'"}),
            'commandType': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'commandUsage': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'description'"}),
            'enabled': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'db_column': "'enabled'"}),
            'eventDetailCommand': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'lastModified'"}),
            'outputFileFormat': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'outputFileFormat'"}),
            'outputLocation': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'outputLocation'"}),
            'replaces': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'db_column': "'replaces'"}),
            'supportedBy': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'db_column': "'supportedBy'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True', 'db_column': "'pk'"}),
            'verificationCommand': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True'})
        },
        u'fpr.commandclassification': {
            'Meta': {'object_name': 'CommandClassification', 'db_table': "u'CommandClassification'"},
            'classification': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'classification'"}),
            'enabled': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'db_column': "'enabled'"}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'db_column': "'lastModified'"}),
            'replaces': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_column': "'replaces'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True', 'db_column': "'pk'"})
        },
        u'fpr.commandrelationship': {
            'Meta': {'object_name': 'CommandRelationship', 'db_table': "u'CommandRelationship'"},
            'command': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True'}),
            'commandClassification': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'enabled': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'db_column': "'enabled'"}),
            'fileID': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'db_column': "'lastModified'"}),
            'replaces': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True', 'db_column': "'pk'"})
        },
        u'fpr.commandssupportedby': {
            'Meta': {'object_name': 'CommandsSupportedBy', 'db_table': "u'CommandsSupportedBy'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'description'"}),
            'enabled': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'db_column': "'enabled'"}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'db_column': "'lastModified'"}),
            'replaces': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'db_column': "'replaces'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True', 'db_column': "'pk'"})
        },
        u'fpr.commandtype': {
            'Meta': {'object_name': 'CommandType', 'db_table': "u'CommandType'"},
            'enabled': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'db_column': "'enabled'"}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'db_column': "'lastModified'"}),
            'replaces': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_column': "'replaces'"}),
            'type': ('django.db.models.fields.TextField', [], {'db_column': "'type'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True', 'db_column': "'pk'"})
        },
        u'fpr.fileid': {
            'Meta': {'object_name': 'FileID', 'db_table': "u'FileID'"},
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'description'"}),
            'enabled': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'db_column': "'enabled'"}),
            'fileidtype': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'db_column': "'fileidtype_id'"}),
            'format': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.FormatVersion']", 'to_field': "'uuid'", 'null': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'db_column': "'lastModified'"}),
            'replaces': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'db_column': "'replaces'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True', 'db_column': "'pk'"}),
            'validaccessformat': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'validAccessFormat'"}),
            'validpreservationformat': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'validPreservationFormat'"})
        },
        u'fpr.fileidsbysingleid': {
            'Meta': {'object_name': 'FileIDsBySingleID', 'db_table': "u'FileIDsBySingleID'"},
            'enabled': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'db_column': "'enabled'"}),
            'fileID': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True'}),
            'id': ('django.db.models.fields.TextField', [], {'db_column': "'id'"}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'db_column': "'lastModified'"}),
            'replaces': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_column': "'replaces'"}),
            'tool': ('django.db.models.fields.TextField', [], {'db_column': "'tool'"}),
            'toolVersion': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'toolVersion'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True', 'db_column': "'pk'"})
        },
        u'fpr.fileidtype': {
            'Meta': {'object_name': 'FileIDType', 'db_table': "u'FileIDType'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'description'"}),
            'enabled': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'db_column': "'enabled'"}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'db_column': "'lastModified'"}),
            'replaces': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_column': "'replaces'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True', 'db_column': "'pk'"})
        },
        u'fpr.format': {
            'Meta': {'ordering': "['group']", 'object_name': 'Format'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.FormatGroup']", 'to_field': "'uuid'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'description'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'})
        },
        u'fpr.formatgroup': {
            'Meta': {'object_name': 'FormatGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'description'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'})
        },
        u'fpr.formatversion': {
            'Meta': {'ordering': "['format', 'description']", 'object_name': 'FormatVersion'},
            'access_format': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'format': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'version_set'", 'to_field': "'uuid'", 'to': u"orm['fpr.Format']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'preservation_format': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'replaces': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.FormatVersion']", 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('format',)", 'max_length': '50', 'populate_from': "'description'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'})
        },
        u'fpr.fprule': {
            'Meta': {'object_name': 'FPRule'},
            'command': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.NormalizationCommand']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'format': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.FormatVersion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'replaces': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.FPRule']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'})
        },
        u'fpr.idcommand': {
            'Meta': {'object_name': 'IDCommand'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'replaces': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.IDCommand']", 'null': 'True', 'blank': 'True'}),
            'script': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'})
        },
        u'fpr.idrule': {
            'Meta': {'object_name': 'IDRule'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'format': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.FormatVersion']", 'to_field': "'uuid'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'replaces': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.IDRule']", 'null': 'True', 'blank': 'True'}),
            'script_output': ('django.db.models.fields.TextField', [], {}),
            'tool': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.IDCommand']", 'to_field': "'uuid'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'})
        },
        u'fpr.idtool': {
            'Meta': {'object_name': 'IDTool'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'_slug'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'fpr.idtoolconfig': {
            'Meta': {'object_name': 'IDToolConfig'},
            'command': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.IDCommand']", 'to_field': "'uuid'"}),
            'config': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'replaces': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.IDToolConfig']", 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('tool',)", 'max_length': '50', 'populate_from': "'config'"}),
            'tool': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'config_set'", 'to_field': "'uuid'", 'to': u"orm['fpr.IDTool']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'})
        },
        u'fpr.normalizationcommand': {
            'Meta': {'object_name': 'NormalizationCommand'},
            'command': ('django.db.models.fields.TextField', [], {}),
            'command_usage': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'event_detail_command': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['fpr.NormalizationCommand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'output_file_format': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'output_location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'replaces': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.NormalizationCommand']", 'null': 'True', 'blank': 'True'}),
            'script_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'supported_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fpr.CommandsSupportedBy']", 'null': 'True', 'blank': 'True'}),
            'tool': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'commands'", 'symmetrical': 'False', 'to': u"orm['fpr.NormalizationTool']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'verification_command': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['fpr.NormalizationCommand']"})
        },
        u'fpr.normalizationtool': {
            'Meta': {'object_name': 'NormalizationTool'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'_slug'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['fpr']