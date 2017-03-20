# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from fpr.models import Format, FormatVersion, IDRule

def data_migration(apps, schema_editor):
    Format.objects.create(description="Jamcracker Tracker Module", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="a198f291-1982-41c8-9025-cee07e6230d3")
    FormatVersion.objects.create(format_id="a198f291-1982-41c8-9025-cee07e6230d3", pronom_id="fmt/975", description="Jamcracker Module", version="None", uuid="1dbe97cb-2797-4c24-a5bb-03b8df244889")
    IDRule.objects.create(format_id="1dbe97cb-2797-4c24-a5bb-03b8df244889", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".jam")

    Format.objects.create(description="MagicaVoxel Vox format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="196bd53d-0e98-4ba6-b40b-cd3a6b002ab3")
    FormatVersion.objects.create(format_id="196bd53d-0e98-4ba6-b40b-cd3a6b002ab3", pronom_id="fmt/976", description="MagicaVoxel", version="None", uuid="fc06b3fa-eff2-4054-b392-3bb881539900")
    IDRule.objects.create(format_id="fc06b3fa-eff2-4054-b392-3bb881539900", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".vox")

    Format.objects.create(description="AutoCAD Design Web Format(DWFx)", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="bad2d3da-86f2-47c4-b6d9-ab8e70a61f6b")
    FormatVersion.objects.create(format_id="bad2d3da-86f2-47c4-b6d9-ab8e70a61f6b", pronom_id="fmt/977", description="AutoCAD Design Web Format(DWFx)", version="None", uuid="f5f2fd37-4107-4626-b074-41589acd4908")
    IDRule.objects.create(format_id="f5f2fd37-4107-4626-b074-41589acd4908", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".dwfx")

    Format.objects.create(description="3DS Max", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="8ea5bdcb-679c-4e2d-bbba-87d10879381f")
    FormatVersion.objects.create(format_id="8ea5bdcb-679c-4e2d-bbba-87d10879381f", pronom_id="fmt/978", description="3DS Max", version="None", uuid="e0bc214c-6e42-4586-bc1c-c2781340cf08")
    IDRule.objects.create(format_id="e0bc214c-6e42-4586-bc1c-c2781340cf08", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".max")

    Format.objects.create(description="XML Property List", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="cff638bd-5b1a-467c-8069-c5f33bf91151")
    FormatVersion.objects.create(format_id="cff638bd-5b1a-467c-8069-c5f33bf91151", pronom_id="fmt/979", description="XML Property List", version="None", uuid="1ff0e01d-c693-44c6-820c-8f9da9dd5648")
    IDRule.objects.create(format_id="1ff0e01d-c693-44c6-820c-8f9da9dd5648", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".plist")

    Format.objects.create(description="AAE Sidecar Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="0da08521-f3ab-468e-ac58-8d5c39092a6d")
    FormatVersion.objects.create(format_id="0da08521-f3ab-468e-ac58-8d5c39092a6d", pronom_id="fmt/980", description="AAE Sidecar Format", version="None", uuid="2862842a-f522-415f-b659-a911bc6355c9")
    IDRule.objects.create(format_id="2862842a-f522-415f-b659-a911bc6355c9", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".aae")

    Format.objects.create(description="EazyDraw File Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="19d29b74-1dcc-4ba7-b8b5-ed92dafd5711")
    FormatVersion.objects.create(format_id="19d29b74-1dcc-4ba7-b8b5-ed92dafd5711", pronom_id="fmt/981", description="EazyDraw File Format", version="None", uuid="07dea117-e934-41aa-abd6-03f6355e1493")
    IDRule.objects.create(format_id="07dea117-e934-41aa-abd6-03f6355e1493", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".ezdraw")

    Format.objects.create(description="iMovieProj File Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="f0ffd839-43a9-485f-b802-54a753268135")
    FormatVersion.objects.create(format_id="f0ffd839-43a9-485f-b802-54a753268135", pronom_id="fmt/982", description="iMovieProj File Format", version="None", uuid="244d70e5-852f-4bff-97f6-a7b939d4d1a2")
    IDRule.objects.create(format_id="244d70e5-852f-4bff-97f6-a7b939d4d1a2", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".iMovieProj")

    Format.objects.create(description="NIB File Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="4d5b172d-e909-480e-a388-7bc2cfad2e3a")
    FormatVersion.objects.create(format_id="4d5b172d-e909-480e-a388-7bc2cfad2e3a", pronom_id="fmt/983", description="NIB File Format", version="None", uuid="17a49c09-7298-4793-8508-c44ab33cd583")
    IDRule.objects.create(format_id="17a49c09-7298-4793-8508-c44ab33cd583", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".nib")

    Format.objects.create(description="Binary Property List", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="6b4f3d42-456a-4ad1-b7f8-f1b94537fa41")
    FormatVersion.objects.create(format_id="6b4f3d42-456a-4ad1-b7f8-f1b94537fa41", pronom_id="fmt/984", description="Binary Property List", version="None", uuid="b357d341-779e-4e4f-9384-e097b49a6a6d")
    IDRule.objects.create(format_id="b357d341-779e-4e4f-9384-e097b49a6a6d", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".plist")

    Format.objects.create(description="Valve Texture Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="972f123f-2ac9-4f5a-b090-8c189d1fa0bd")
    FormatVersion.objects.create(format_id="972f123f-2ac9-4f5a-b090-8c189d1fa0bd", pronom_id="fmt/985", description="Valve Texture Format little endian", version="None", uuid="6c8df6d2-6033-4a17-92a8-f2e41e37bc90")
    IDRule.objects.create(format_id="6c8df6d2-6033-4a17-92a8-f2e41e37bc90", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".vtf")

    Format.objects.create(description="Extensible Metadata Platform Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="d2358398-05d9-408c-949e-fa0f2c0d967f")
    FormatVersion.objects.create(format_id="d2358398-05d9-408c-949e-fa0f2c0d967f", pronom_id="fmt/986", description="XMP file format", version="None", uuid="0080474c-9fc8-4a5c-8d20-dc9abdf30baa")
    IDRule.objects.create(format_id="0080474c-9fc8-4a5c-8d20-dc9abdf30baa", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".xmp")

    Format.objects.create(description="Microsoft OneNote Package File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="88bcf34c-b567-4258-89cc-a31aabbfc7ed")
    FormatVersion.objects.create(format_id="88bcf34c-b567-4258-89cc-a31aabbfc7ed", pronom_id="fmt/987", description="OneNote package file", version="None", uuid="fcd88ab0-289c-47eb-9b7b-dd7dc8ddbf33")
    IDRule.objects.create(format_id="fcd88ab0-289c-47eb-9b7b-dd7dc8ddbf33", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".onepkg")

    Format.objects.create(description="ESRI ArcScene Document", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="afe4931c-4bdc-425e-b851-c2b8b3b203b3")
    FormatVersion.objects.create(format_id="afe4931c-4bdc-425e-b851-c2b8b3b203b3", pronom_id="fmt/988", description="ESRI ArcScene Document", version="None", uuid="850f2aeb-1f38-4655-aed4-ade5dac815f5")
    IDRule.objects.create(format_id="850f2aeb-1f38-4655-aed4-ade5dac815f5", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".sxd")

    Format.objects.create(description="ESRI ArcGlobe Document", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="1bf306e0-eafd-41a2-a03f-37fe1647f79c")
    FormatVersion.objects.create(format_id="1bf306e0-eafd-41a2-a03f-37fe1647f79c", pronom_id="fmt/989", description="ESRI ArcGlobe Document", version="None", uuid="fd65d8d6-e99f-4c67-b866-6813bb311c27")
    IDRule.objects.create(format_id="fd65d8d6-e99f-4c67-b866-6813bb311c27", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".3dd")

    Format.objects.create(description="ESRI File Geodatabase", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="97eef473-05ae-4c93-905c-f86502310a57")
    FormatVersion.objects.create(format_id="97eef473-05ae-4c93-905c-f86502310a57", pronom_id="fmt/990", description="ESRI File Geodatabase", version="None", uuid="8099ed5b-bd84-4d75-8f68-667f999e3962")

    Format.objects.create(description="SHA256 File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="812ab617-b46f-4e1e-b63d-d18520b2725d")
    FormatVersion.objects.create(format_id="812ab617-b46f-4e1e-b63d-d18520b2725d", pronom_id="fmt/991", description="SHA256 File", version="None", uuid="65b470b8-4cc6-4ad0-bdae-0a1d4f6a298e")
    IDRule.objects.create(format_id="65b470b8-4cc6-4ad0-bdae-0a1d4f6a298e", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".sha256")

    Format.objects.create(description="SHA1 File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="4e9e3f4b-e256-4934-b5dd-8cda480a7b45")
    FormatVersion.objects.create(format_id="4e9e3f4b-e256-4934-b5dd-8cda480a7b45", pronom_id="fmt/992", description="SHA1 File", version="None", uuid="8ed521e4-24dc-449d-a64c-5138e5355821")
    IDRule.objects.create(format_id="8ed521e4-24dc-449d-a64c-5138e5355821", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".sha1")

    Format.objects.create(description="MD5 File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="04c1bbce-7f5a-4889-8337-bd2d3992e7a0")
    FormatVersion.objects.create(format_id="04c1bbce-7f5a-4889-8337-bd2d3992e7a0", pronom_id="fmt/993", description="MD5 File", version="None", uuid="c0184256-fbc1-4fa3-85a7-089204f4ae81")
    IDRule.objects.create(format_id="c0184256-fbc1-4fa3-85a7-089204f4ae81", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".md5")

    Format.objects.create(description="Jeffs Image Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="4f3e65dc-34e1-43b3-b6bb-fe87e728ed74")
    FormatVersion.objects.create(format_id="4f3e65dc-34e1-43b3-b6bb-fe87e728ed74", pronom_id="fmt/994", description="Jeffs Image Format", version="None", uuid="d1b54dd9-c12d-44d4-b2c4-e5be00c5c76d")
    IDRule.objects.create(format_id="d1b54dd9-c12d-44d4-b2c4-e5be00c5c76d", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".jif")

    FormatVersion.objects.create(format_id="c1f2a84f-fd6b-40de-8d7c-dd2bae449232", pronom_id="fmt/995", description="SIARD (Software-Independent Archiving of Relational Databases)", version="2.0", uuid="3a361243-a527-4ace-9d06-4385b061e3c4")
    IDRule.objects.create(format_id="3a361243-a527-4ace-9d06-4385b061e3c4", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".siard")



class Migration(migrations.Migration):

    dependencies = [
        ('fpr', '0006_i18n_models'),
    ]

    operations = [
        migrations.RunPython(data_migration),
    ]
