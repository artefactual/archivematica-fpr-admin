# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os

from django.db import migrations, models


HERE = os.path.dirname(os.path.abspath(__file__))
MIGR_DATA = os.path.join(os.path.dirname(HERE), 'migrations-data')
POLICY_CHECK_CMD_FNM = os.path.join(MIGR_DATA, 'mc_policy_check_cmd.py')


def data_migration(apps, schema_editor):
    """FPR tool, commands, and rules for MediaConch policy checks.

    Creates the following:

    - MediaConch FPCommand for policy checks (using
        migrations-data/mc_policy_check_cmd.py)
    - MediaConch FPRule for checking .mkv preservation derivatives against a
        policy
    """

    FPTool = apps.get_model('fpr', 'FPTool')
    FPCommand = apps.get_model('fpr', 'FPCommand')
    FPRule = apps.get_model('fpr', 'FPRule')
    FormatVersion = apps.get_model('fpr', 'FormatVersion')
    mkv_format = FormatVersion.objects.get(description='Generic MKV')

    # MediaConch Tool
    mediaconch_tool = FPTool.objects.get(description='MediaConch')

    # MediaConch Policy Check Command
    # NOTE: this command is disabled by default because it references a
    # dummy/non-existent policy file.
    with open(POLICY_CHECK_CMD_FNM) as filei:
        mediaconch_policy_check_command_script = filei.read()
    mediaconch_policy_check_command_uuid = \
        '9ef290f7-5320-4d69-821a-3156fc184b4e'
    mediaconch_policy_check_command = FPCommand.objects.create(
        uuid=mediaconch_policy_check_command_uuid,
        tool=mediaconch_tool,
        description=('Check against policy PLACEHOLDER_FOR_POLICY_FILE_NAME'
                     ' using MediaConch'),
        command=mediaconch_policy_check_command_script,
        script_type='pythonScript',
        command_usage='validation',
        enabled=False
    )

    # MediaConch-against-MKV-for-policyCheckingPreservationFile Rule.
    # Create the FPR rule that causes 'Check against policy using MediaConch'
    # command to be used on 'Generic MKV' files intended for preservation in
    # the "Policy check" micro-service.
    # NOTE: this rule is disabled by default because it references a disabled
    # command that, in turn, references a non-existent MediaConch policy file.
    policy_check_preservation_rule_pk = 'aaaf34ef-c00f-4bb9-85c1-01c0ad5f3a8c'
    FPRule.objects.create(
        uuid=policy_check_preservation_rule_pk,
        purpose='policy_check',
        command=mediaconch_policy_check_command,
        format=mkv_format,
        enabled=False
    )


class Migration(migrations.Migration):

    dependencies = [
        ('fpr', '0005_mediaconch_validation'),
    ]

    FPRULE_CHOICES = [
        (b'access', b'Access'),
        (b'characterization', b'Characterization'),
        (b'extract', b'Extract'),
        (b'preservation', b'Preservation'),
        (b'thumbnail', b'Thumbnail'),
        (b'transcription', b'Transcription'),
        (b'validation', b'Validation'),
        (b'policy_check', b'Validation against a Policy'),
        (b'default_access', b'Default Access'),
        (b'default_characterization', b'Default Characterization'),
        (b'default_thumbnail', b'Default Thumbnail')
    ]

    operations = [
        migrations.AlterField(
            model_name='fprule',
            name='purpose',
            field=models.CharField(max_length=32, choices=FPRULE_CHOICES)
        ),
        migrations.RunPython(data_migration),
    ]
