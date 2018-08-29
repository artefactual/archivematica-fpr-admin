# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.core.management import call_command
from django.db import migrations

def data_migration(apps, schema_editor):
    fixture_file = os.path.join(os.path.dirname(__file__), 'pronom_93.json')
    call_command('loaddata', fixture_file, app_label='fpr')

    Format = apps.get_model('fpr', 'Format')
    FormatVersion = apps.get_model('fpr', 'FormatVersion')

    FormatVersion.objects.create(format_id="9b3f9406-a375-4b66-9081-61a317e68cbf", pronom_id="x-fmt/395", description="WordPerfect Graphics 1.0", version="1.0", uuid="ec196238-2461-4066-bd05-ee9210286e7e")
    IDRule.objects.filter(command_output=".wpg").delete()

    FormatVersion.objects.create(format_id="9b3f9406-a375-4b66-9081-61a317e68cbf", pronom_id="fmt/1042", description="WordPerfect Graphics 2.0", version="2.0", uuid="82cad44c-0f23-4fc9-b7b7-d08ce2e48511")
    IDRule.objects.create(format_id="82cad44c-0f23-4fc9-b7b7-d08ce2e48511", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".wpg")

    FormatVersion.objects.create(format_id="1a91d8c5-7bfb-47b1-9e4c-8dd934f33cda", pronom_id="fmt/1083", description="HWP 3", version="3", uuid="938fec89-28f5-4448-bbd0-fdcf298ad3e1")
    IDRule.objects.filter(command_output=".hwp").delete()

    Format.objects.create(description="High Efficiency Image File Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="7960e5c5-4ef6-4696-a86f-f6314fb6cee4")
    FormatVersion.objects.create(format_id="7960e5c5-4ef6-4696-a86f-f6314fb6cee4", pronom_id="fmt/1101", description="HEIF", version="None", uuid="6fdfc554-be9b-48c7-89cc-5f24c4037564")
    IDRule.objects.create(format_id="6fdfc554-be9b-48c7-89cc-5f24c4037564", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".heic")

    Format.objects.create(description="Uuencoded File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="39f76e57-7ca6-4fc3-8255-6b1983c36d1e")
    FormatVersion.objects.create(format_id="39f76e57-7ca6-4fc3-8255-6b1983c36d1e", pronom_id="fmt/1102", description="Uuencoded File", version="None", uuid="3965d5b1-9bcb-481a-94de-6ab8cc211613")
    IDRule.objects.create(format_id="3965d5b1-9bcb-481a-94de-6ab8cc211613", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".uue")

    Format.objects.create(description="AutoCAD Hatch Pattern", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="7ae13d51-3b0c-4c16-99e4-f4af017183a0")
    FormatVersion.objects.create(format_id="7ae13d51-3b0c-4c16-99e4-f4af017183a0", pronom_id="fmt/1103", description="AutoCAD Hatch Pattern", version="None", uuid="8a23ff45-a242-4903-a4ce-c890bc24b986")
    IDRule.objects.filter(command_output=".pat").delete()

    Format.objects.create(description="Seattle FilmWorks SFW Image Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="409d3125-70e2-4b57-a8ec-c66f928f2b35")
    FormatVersion.objects.create(format_id="409d3125-70e2-4b57-a8ec-c66f928f2b35", pronom_id="fmt/1104", description="Seattle FilmWorks Image", version="None", uuid="1ca63c57-d939-4e78-b645-ba308f82ae6b")
    IDRule.objects.create(format_id="1ca63c57-d939-4e78-b645-ba308f82ae6b", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".sfw")

    Format.objects.create(description="Hierarchical File System", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="96f8ae5f-5607-4a3c-ad3c-98061f45e136")
    FormatVersion.objects.create(format_id="96f8ae5f-5607-4a3c-ad3c-98061f45e136", pronom_id="fmt/1105", description="HFS", version="None", uuid="a9af79c4-7604-4a87-85c0-96384282417e")
    IDRule.objects.filter(command_output=".img").delete()

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1106", description="PYC 2.0", version="2.0", uuid="0c425ebe-93cc-4754-8550-bfc252f0ec98")
    IDRule.objects.filter(command_output=".pyc").delete()

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1107", description="PYC 2.1", version="2.1", uuid="60108ba6-637e-4e0c-98fe-c44228a5156a")
    IDRule.objects.create(format_id="60108ba6-637e-4e0c-98fe-c44228a5156a", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".pyc")

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1108", description="PYC 2.2", version="2.2", uuid="c6ab0f62-7a4f-4e3c-a9e0-e6a047ce2167")
    IDRule.objects.filter(command_output=".pyc").delete()

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1109", description="PYC 2.3", version="2.3", uuid="35eee8c9-47fd-4589-aec0-95d456da42a9")
    IDRule.objects.create(format_id="35eee8c9-47fd-4589-aec0-95d456da42a9", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".pyc")

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1110", description="PYC 2.4", version="2.4", uuid="ce344dd5-04e3-48a3-baa6-cb761f9941e3")
    IDRule.objects.filter(command_output=".pyc").delete()

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1111", description="PYC 2.5", version="2.5", uuid="fbf5ca65-2c9b-4785-a5c3-ff0ee124f0e4")
    IDRule.objects.create(format_id="fbf5ca65-2c9b-4785-a5c3-ff0ee124f0e4", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".pyc")

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1112", description="PYC 2.6", version="2.6", uuid="9ea8efed-58fc-4ed8-be19-5a7a4dbbafb9")
    IDRule.objects.filter(command_output=".pyc").delete()

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1113", description="PYC 3.0", version="3.0", uuid="2ed66013-63d0-4a32-a80f-4f36252030c9")
    IDRule.objects.create(format_id="2ed66013-63d0-4a32-a80f-4f36252030c9", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".pyc")

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1114", description="PYC 3.1", version="3.1", uuid="aec826de-750f-4ebf-ad67-14743ea7a554")
    IDRule.objects.filter(command_output=".pyc").delete()

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1115", description="PYC 3.2", version="3.2", uuid="b7a66cee-e963-475d-b896-28c4f87c3ab6")
    IDRule.objects.create(format_id="b7a66cee-e963-475d-b896-28c4f87c3ab6", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".pyc")

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1116", description="PYC 3.3", version="3.3", uuid="d53c26c3-13b8-4eaa-834b-958829cc319e")
    IDRule.objects.filter(command_output=".pyc").delete()

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1117", description="PYC 3.5", version="3.5", uuid="b290d8ab-ce60-4867-9ce5-4383f0222e14")
    IDRule.objects.create(format_id="b290d8ab-ce60-4867-9ce5-4383f0222e14", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".pyc")

    FormatVersion.objects.create(format_id="97b61063-eb03-4310-83cf-6df81f7d1c3f", pronom_id="fmt/1118", description="PYC 3.6", version="3.6", uuid="3626ea73-f50e-49b1-85fe-cb8c8634d1ec")
    IDRule.objects.filter(command_output=".pyc").delete()

    Format.objects.create(description="Jupyter Python Notebook", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="a15d7dc8-41b7-4f0b-bf66-2e1d308bffd8")
    FormatVersion.objects.create(format_id="a15d7dc8-41b7-4f0b-bf66-2e1d308bffd8", pronom_id="fmt/1119", description="Jupyter Python Notebook", version="None", uuid="54de5301-ca7e-4ca5-85b9-b0eb531aa457")
    IDRule.objects.create(format_id="54de5301-ca7e-4ca5-85b9-b0eb531aa457", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".ipynb")

    Format.objects.create(description="DIFFRACplus Raw Data File Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="09c17878-1b46-4df3-9d7d-28485df23471")
    FormatVersion.objects.create(format_id="09c17878-1b46-4df3-9d7d-28485df23471", pronom_id="fmt/1120", description="DIFFRACplus Raw Data File Format 1", version="1", uuid="d3e76282-3e47-40f4-972a-d490d977dbf5")
    IDRule.objects.filter(command_output=".raw").delete()

    FormatVersion.objects.create(format_id="09c17878-1b46-4df3-9d7d-28485df23471", pronom_id="fmt/1121", description="DIFFRACplus Raw Data File Format 2", version="2", uuid="8026ce75-0c34-4fa3-b380-5ef5e6103c05")
    IDRule.objects.create(format_id="8026ce75-0c34-4fa3-b380-5ef5e6103c05", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".raw")

    Format.objects.create(description="VAMAS Surface Chemical Analysis Standard Data Transfer Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="19b477db-5fca-4002-9f69-67ec7ff3fcbd")
    FormatVersion.objects.create(format_id="19b477db-5fca-4002-9f69-67ec7ff3fcbd", pronom_id="fmt/1122", description="VAMAS Surface Chemical Analysis Standard Data Transfer Format", version="None", uuid="f38780e8-f358-4753-a732-61b5b68dfffb")
    IDRule.objects.create(format_id="f38780e8-f358-4753-a732-61b5b68dfffb", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".vms")

    Format.objects.create(description="Origin Project Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="cf6ea57a-7731-43d7-8fcd-0a7a1b73771e")
    FormatVersion.objects.create(format_id="cf6ea57a-7731-43d7-8fcd-0a7a1b73771e", pronom_id="fmt/1123", description="Origin Project Format Non-Unicode", version="", uuid="c2896c5e-2a6b-4def-85e3-044e19067e08")
    IDRule.objects.create(format_id="c2896c5e-2a6b-4def-85e3-044e19067e08", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".opj")

    FormatVersion.objects.create(format_id="cf6ea57a-7731-43d7-8fcd-0a7a1b73771e", pronom_id="fmt/1124", description="Origin Project Format Unicode", version="Unicode", uuid="816d0e5c-fa96-4172-9cdb-597479b16785")
    IDRule.objects.create(format_id="816d0e5c-fa96-4172-9cdb-597479b16785", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".opju")

    Format.objects.create(description="JASCO JWS Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="070ea840-c87b-4880-96f9-bf05cf51bbc2")
    FormatVersion.objects.create(format_id="070ea840-c87b-4880-96f9-bf05cf51bbc2", pronom_id="fmt/1125", description="JASCO JWS Format", version="OLE2", uuid="e6ab7cf2-47c0-40f6-b586-a8ce8402daae")
    IDRule.objects.create(format_id="e6ab7cf2-47c0-40f6-b586-a8ce8402daae", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".jws")

    Format.objects.create(description="Sony SR2 RAW Image File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="fb5fa919-9935-4cd3-a957-a8ae59e73395")
    FormatVersion.objects.create(format_id="fb5fa919-9935-4cd3-a957-a8ae59e73395", pronom_id="fmt/1126", description="Sony SR2", version="None", uuid="36f8495a-f1d5-47c2-b15e-a2a826d2ca8c")
    IDRule.objects.create(format_id="36f8495a-f1d5-47c2-b15e-a2a826d2ca8c", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".sr2")

    Format.objects.create(description="Sony ARW RAW Image File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="0b9ba339-14fc-46f2-8a06-561c63fdd7c6")
    FormatVersion.objects.create(format_id="0b9ba339-14fc-46f2-8a06-561c63fdd7c6", pronom_id="fmt/1127", description="Sony ARW 2.x", version="2.x", uuid="f446e519-b410-4727-9b4c-982357af6227")
    IDRule.objects.filter(command_output=".arw").delete()

    Format.objects.create(description="Progressive Graphics File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="84170459-2453-46da-b6b4-241a6aa57824")
    FormatVersion.objects.create(format_id="84170459-2453-46da-b6b4-241a6aa57824", pronom_id="fmt/1128", description="Progressive Graphics File", version="None", uuid="18f9d421-0cc4-4720-98ec-6ab48b6c86fa")
    IDRule.objects.create(format_id="18f9d421-0cc4-4720-98ec-6ab48b6c86fa", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".pgf")

    Format.objects.create(description="PDF 2.0 - Portable Document Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="f08a4e9f-fc46-4cdb-9079-85cfbdc4e791")
    FormatVersion.objects.create(format_id="f08a4e9f-fc46-4cdb-9079-85cfbdc4e791", pronom_id="fmt/1129", description="PDF 2.0", version="2.0", uuid="a9716916-f368-4a3a-94b0-58b3266a48cd")
    IDRule.objects.filter(command_output=".pdf").delete()

    Format.objects.create(description="C3D File Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="56c3dd5d-6589-4232-a056-eff2694fe397")
    FormatVersion.objects.create(format_id="56c3dd5d-6589-4232-a056-eff2694fe397", pronom_id="fmt/1130", description="C3D", version="None", uuid="d88cdd04-2455-4779-8c98-f9d3a05b6ede")
    IDRule.objects.create(format_id="d88cdd04-2455-4779-8c98-f9d3a05b6ede", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".c3d")

    Format.objects.create(description="Gatan Digital Micrograph File Format (DM3)", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="917ccafd-b45e-4a73-b253-8f8fb4c00d15")
    FormatVersion.objects.create(format_id="917ccafd-b45e-4a73-b253-8f8fb4c00d15", pronom_id="fmt/1131", description="Gatan Digital Micrograph 3", version="3", uuid="e64e8666-3495-45b7-8fb2-681f6a492290")
    IDRule.objects.create(format_id="e64e8666-3495-45b7-8fb2-681f6a492290", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".dm3")


class Migration(migrations.Migration):

    dependencies = [
        ('fpr', '0016_update_idtools'),
    ]

    operations = [
	    migrations.RunPython(data_migration),
    ]
