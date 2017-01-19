# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpr', '0004_pronom_88'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fprule',
            name='purpose',
            field=models.CharField(max_length=32, choices=[(b'access', b'Access'), (b'characterization', b'Characterization'), (b'extract', b'Extract'), (b'preservation', b'Preservation'), (b'thumbnail', b'Thumbnail'), (b'transcription', b'Transcription'), (b'validation', b'Validation'), (b'validatePreservationDerivative', b'Validation of Preservation Derivatives'), (b'validateAccessDerivative', b'Validation of Access Derivatives'), (b'checkingPresDerivativePolicy', b'Validation of Preservation Derivatives against a Policy'), (b'checkingAccessDerivativePolicy', b'Validation of Access Derivatives against a Policy'), (b'checkingOriginalPolicy', b'Validation of Originals against a Policy'), (b'default_access', b'Default Access'), (b'default_characterization', b'Default Characterization'), (b'default_thumbnail', b'Default Thumbnail')]),
        ),
    ]
