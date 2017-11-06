# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


def data_migration(apps, schema_editor):
    """Migration that causes each OCR text file to include the UUID of its
    source file in its filename. This prevents OCR text files from overwriting
    one another when there are two identically named source files in a
    transfer. See
    https://github.com/artefactual/archivematica-fpr-admin/issues/66
    """
    IDCommand = apps.get_model('fpr', 'IDCommand')
    ocr_command = IDCommand.objects.get(
        uuid='5d501dbf-76bb-4569-a9db-9e367800995e')
    ocr_command.command = (
        'ocrfiles="%SIPObjectsDirectory%metadata/OCRfiles"\n'
        'test -d "$ocrfiles" || mkdir -p "$ocrfiles"\n\n'
        'tesseract %fileFullName% "$ocrfiles/%fileName%-%fileUUID%"')
    ocr_command.output_location = (
        '%SIPObjectsDirectory%metadata/OCRfiles/%fileName%-%fileUUID%.txt')
    ocr_command.save()


class Migration(migrations.Migration):

    dependencies = [
        ('fpr', '0016_update_idtools'),
    ]

    operations = [
        migrations.RunPython(data_migration),
    ]
