"""Migration that modifies the workflow to be able to identify, characterize
and extract disk images containing HFS file systems.

"""

from __future__ import print_function, unicode_literals
import os

from django.db import migrations


HERE = os.path.dirname(os.path.abspath(__file__))
MIGR_DATA = os.path.join(os.path.dirname(HERE), 'migrations-data')

HFS2DFXML_CMD_FNM = 'fiwalk_fallback_hfs2dfxml.py'
HFS2DFXML_CMD_FPTH = os.path.join(MIGR_DATA, HFS2DFXML_CMD_FNM)

TSKR_UNHFS_CMD_FNM = 'tsk_recover_fallback_unhfs.py'
TSKR_UNHFS_CMD_FPTH = os.path.join(MIGR_DATA, TSKR_UNHFS_CMD_FNM)

SGFRD_FNM = 'siegfried_identify_new.py'
SGFRD_FPTH = os.path.join(MIGR_DATA, SGFRD_FNM)


def data_migration(apps, schema_editor):
    """Modify the FPR so that disk images containing HFS file systems can be
    identified, characterized and extracted.

    1. create FPTool for hfs2dfxml
    2. create FPTool for hfsexplorer
    3. create FPCommand that characterizes using fiwalk and falls back to
       hfs2dfxml
    4. create FPCommand that extracts using tsk_recover and falls back to unhfs
    5. update Siegfried IDTool to use blkid to identify HFS disk images
    6. create special FormatVersion for UCLA HFS Disk Image
    7. create special FormatVersion for NYPL HFS Disk Image
    8. create IDRule linking the new Siegfried identification command to the
       new UCLA HFS FormatVersion.
    """

    Format = apps.get_model('fpr', 'Format')
    FormatGroup = apps.get_model('fpr', 'FormatGroup')
    FormatVersion = apps.get_model('fpr', 'FormatVersion')
    FPCommand = apps.get_model('fpr', 'FPCommand')
    FPRule = apps.get_model('fpr', 'FPRule')
    FPTool = apps.get_model('fpr', 'FPTool')
    IDCommand = apps.get_model('fpr', 'IDCommand')
    IDRule = apps.get_model('fpr', 'IDRule')
    IDTool = apps.get_model('fpr', 'IDTool')

    json_format = FormatVersion.objects.get(
        description='JSON Data Interchange Format')
    xml_format = FormatVersion.objects.get(
        description='XML', version='1.0')
    sleuthkit_tool = FPTool.objects.get(description='Sleuthkit')

    # Create a new FPR tool for hfs2dfxml (characterization)
    hfs2dfxml_tool_uuid = '1f334733-867e-4c8c-a6a6-b667bcb2f890'
    FPTool.objects.create(
        uuid=hfs2dfxml_tool_uuid,
        description='hfs2dfxml',
        version='0.1.0',
        slug='hfs2dfxml-010'
    )

    # Create a new FPR tool for hfsexplorer (extraction)
    hfsexplorer_tool_uuid = '0a0685ab-b823-4e18-8a31-8234c4ce3814'
    FPTool.objects.create(
        uuid=hfsexplorer_tool_uuid,
        description='hfsexplorer',
        version='0.23.1',
        slug='hfsexplorer-0231'
    )

    # Command: characterization: "Fiwalk fallback hfs2dfxml"
    with open(HFS2DFXML_CMD_FPTH) as filei:
        hfs2dfxml_command_script = filei.read()
    hfs2dfxml_command_uuid = (
        'e8d971f4-9c14-4b60-913e-33fe7a2a9c3e')
    hfs2dfxml_command = FPCommand.objects.create(
        uuid=hfs2dfxml_command_uuid,
        # We use the Sleuthkit tool for this command because it's the tool
        # corresponding to fiwalk. Since the tool(s) used for characterization
        # are not explicitly documented in the METS file, this is ok for now,
        # even though it is inaccurate in the cases where hfs2dfxml actually
        # gets used.
        tool=sleuthkit_tool,
        description='fiwalk fallback to hfs2dfxml',
        command=hfs2dfxml_command_script,
        script_type='pythonScript',
        command_usage='characterization',
        output_format=xml_format
    )

    # Command: extraction: "tsk_recover fallback unhfs"
    with open(TSKR_UNHFS_CMD_FPTH) as filei:
        tskr_unhfs_command_script = filei.read()
    tskr_unhfs_command_uuid = (
        '672a12d8-70a8-45f8-aa13-3a4c86cf1a4b')
    tskr_unhfs_command = FPCommand.objects.create(
        uuid=tskr_unhfs_command_uuid,
        # We use the Sleuthkit tool for this command because it's the tool
        # corresponding to tsk_recover. The JSON output by the command itself
        # will trigger the extractContents.py client script into setting the
        # tool used to hfsexplorer in those cases where unhfs.sh was used to
        # extract a HFS disk image.
        tool=sleuthkit_tool,
        description=('tsk_recover fallback unhfs'),
        command=tskr_unhfs_command_script,
        script_type='pythonScript',
        command_usage='extraction',
        output_format=json_format
    )

    # Update the Siegfried identification command so that it uses blkid to
    # identify HFS disk images.
    sgfd_tool = IDTool.objects.get(
        enabled=True,
        description='Siegfried')
    current_sgfd_cmd = IDCommand.objects.get(
        enabled=True,
        description='Identify using Siegfried')
    with open(SGFRD_FPTH) as filei:
        new_sgfd_script = filei.read()
    IDCommand.objects\
        .filter(
            enabled=True,
            description='Identify using Siegfried')\
        .update(enabled=False)
    new_sgfd_cmd_uuid = (
        'b8a39a9a-3fd9-4519-8f2c-c5247cc36ecf')
    new_sgfd_cmd = IDCommand.objects.create(
        uuid=new_sgfd_cmd_uuid,
        description='Identify using Siegfried',
        enabled=True,
        config='PUID',
        script=new_sgfd_script,
        script_type='pythonScript',
        tool=sgfd_tool,
        replaces=current_sgfd_cmd
    )

    disk_image_group = FormatGroup.objects.get(
        description='Disk Image')

    # Create "HFS Disk Image (HFS filesystem)" Format.
    hfs_format_uuid = (
        'e907ae61-e5d3-46b2-af74-c29633c7ce22')
    hfs_format = Format.objects.create(
        uuid=hfs_format_uuid,
        description='HFS Disk Image (HFS filesystem)',
        group=disk_image_group,
        slug='hfs-disk-image'
    )

    # Create "HFS Disk Image" Format version.
    hfs_format_version_uuid = (
        '1a0f0454-8104-41a3-bf59-294f1cdb4050')
    hfs_format_version = FormatVersion.objects.create(
        uuid=hfs_format_version_uuid,
        format=hfs_format,
        description='HFS Disk Image',
        pronom_id='archivematica-fmt/6',
        slug='hfs-disk-image'
    )

    # Create FPR rule that causes "HFS Disk Image" format versions to be
    # characterized using "Fiwalk fallback hfs2dfxml".
    # INSERT INTO fpr_fprule (enabled, lastmodified, uuid, purpose, count_attempts, count_okay, count_not_okay, command_id, format_id) VALUES (1, '2017-05-09 12:00:00', 'f5eb68f5-291b-4cf0-befe-5ab8aa54952e', 'characterization', 0, 0, 0, 'e8d971f4-9c14-4b60-913e-33fe7a2a9c3e', '1a0f0454-8104-41a3-bf59-294f1cdb4050');
    FPRule.objects.create(
        uuid='f5eb68f5-291b-4cf0-befe-5ab8aa54952e',
        purpose='characterization',
        command=hfs2dfxml_command,
        format=hfs_format_version
    )

    # Create FPR rule that causes "HFS Disk Image" format versions to be
    # extracted using "tsk_recover fallback unhfs".
    # INSERT INTO fpr_fprule (enabled, lastmodified, uuid, purpose, count_attempts, count_okay, count_not_okay, command_id, format_id) VALUES (1, '2017-05-09 12:00:00', '0579817f-6c32-46b1-a9b1-4867339d84d9', 'extract', 0, 0, 0, '672a12d8-70a8-45f8-aa13-3a4c86cf1a4b', '1a0f0454-8104-41a3-bf59-294f1cdb4050');
    FPRule.objects.create(
        uuid='0579817f-6c32-46b1-a9b1-4867339d84d9',
        purpose='extract',
        command=tskr_unhfs_command,
        format=hfs_format_version
    )

    # Update characterization rule to use "fiwalk fallback hfs2dfxml" for
    # archivematica-fmt/4.
    FPRule.objects.filter(
        enabled=True,
        format__pronom_id='archivematica-fmt/4',
        purpose='characterization'
    ).update(command=hfs2dfxml_command)

    # Update extraction rule to use "tsk_recover fallback unhfs" for
    # archivematica-fmt/4.
    FPRule.objects.filter(
        enabled=True,
        format__pronom_id='archivematica-fmt/4',
        purpose='extract'
    ).update(command=tskr_unhfs_command)


class Migration(migrations.Migration):

    dependencies = [
        ('fpr', '0014_fix_fits_command'),
    ]

    operations = [
        migrations.RunPython(data_migration)
    ]
