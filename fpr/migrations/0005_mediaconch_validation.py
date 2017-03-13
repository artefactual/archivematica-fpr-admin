# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os

from django.db import migrations, models


HERE = os.path.dirname(os.path.abspath(__file__))
MIGR_DATA = os.path.join(os.path.dirname(HERE), 'migrations-data')
VALIDATE_CMD_FNM = os.path.join(MIGR_DATA, 'mc_validate_cmd.py')


def data_migration(apps, schema_editor):
    """FPR tool, commands, and rules for MediaConch file validation (i.e., .mkv
    implementation checks)

    Creates the following:

    - MediaConch FPTool
    - MediaConch FPCommand for validation (using
        migrations-data/mc_validate_cmd.py)
    - MediaConch FPRule for validation of .mkv using above command
    - MediaConch FPRule for validation of .mkv preservation derivatives using
        above command
    - MediaConch FPRule for validation of .mkv access derivatives using
        above command
    """

    FPTool = apps.get_model('fpr', 'FPTool')
    FPCommand = apps.get_model('fpr', 'FPCommand')
    FPRule = apps.get_model('fpr', 'FPRule')
    FormatVersion = apps.get_model('fpr', 'FormatVersion')
    mkv_format = FormatVersion.objects.get(description='Generic MKV')

    # MediaConch Tool
    mediaconch_tool_uuid = 'f79c56f1-2d42-440a-8a1f-f40888e24bca'
    mediaconch_tool = FPTool.objects.create(
        uuid=mediaconch_tool_uuid,
        description='MediaConch',
        version='16.12',
        enabled=True,
        slug='mediaconch-1612'
    )

    # MediaConch Validation Command
    with open(VALIDATE_CMD_FNM) as filei:
        mediaconch_command_script = filei.read()
    mediaconch_command_uuid = '287656fb-e58f-4967-bf72-0bae3bbb5ca8'
    mediaconch_command = FPCommand.objects.create(
        uuid=mediaconch_command_uuid,
        tool=mediaconch_tool,
        description='Validate using MediaConch',
        command=mediaconch_command_script,
        script_type='pythonScript',
        command_usage='validation'
    )

    # MediaConch-against-MKV-for-validate Rule.
    mediaconch_mkv_rule_uuid = 'a2fb0477-6cde-43f8-a1c9-49834913d588'
    FPRule.objects.create(
        uuid=mediaconch_mkv_rule_uuid,
        purpose='validation',
        command=mediaconch_command,
        format=mkv_format
    )

    # MediaConch-against-MKV-for-validatePreservationDerivative Rule.
    # Create the FPR rule that causes 'Validate using MediaConch' command to be
    # used on for-preservation-derived 'Generic MKV' files in the "Validate
    # Preservation Derivatives" micro-service.
    vldt_prsrvtn_drvtv_rule_pk = '3fcbf5d2-c908-4ec4-b618-8c7dc0f4117e'
    FPRule.objects.create(
        uuid=vldt_prsrvtn_drvtv_rule_pk,
        purpose='validatePreservationDerivative',
        command=mediaconch_command,
        format=mkv_format
    )

    # MediaConch-against-MKV-for-validateAccessDerivative Rule.
    # Create the FPR rule that causes 'Validate using MediaConch' command to be
    # used on for-access-derived 'Generic MKV' files in the "Validate
    # Access Derivatives" micro-service.
    vldt_ccss_drvtv_rule_pk = '0ada4f48-d8a6-4762-8a20-c04cb4e58676'
    FPRule.objects.create(
        uuid=vldt_ccss_drvtv_rule_pk,
        purpose='validateAccessDerivative',
        command=mediaconch_command,
        format=mkv_format
    )


class Migration(migrations.Migration):

    dependencies = [
        ('fpr', '0004_pronom_88'),
    ]

    FPRULE_CHOICES = [
        (b'access', b'Access'),
        (b'characterization', b'Characterization'),
        (b'extract', b'Extract'),
        (b'preservation', b'Preservation'),
        (b'thumbnail', b'Thumbnail'),
        (b'transcription', b'Transcription'),
        (b'validation', b'Validation'),
        (b'validatePreservationDerivative', b'Validation of Preservation Derivatives'),
        (b'validateAccessDerivative', b'Validation of Access Derivatives'),
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
