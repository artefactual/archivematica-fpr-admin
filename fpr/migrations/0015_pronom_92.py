# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def data_migration(apps, schema_editor):
    Format = apps.get_model('fpr', 'Format')
    FormatVersion = apps.get_model('fpr', 'FormatVersion')
    IDRule = apps.get_model('fpr', 'IDRule')

    Format.objects.create(description="HDF", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="047edfb6-f85e-41d6-9d0f-8b48aa92d7e4")
    FormatVersion.objects.create(format_id="047edfb6-f85e-41d6-9d0f-8b48aa92d7e4", pronom_id="fmt/1041", description="HDF 1-4", version="1-4", uuid="4d5f40e1-b4f3-4406-9adf-38d310254062")
    IDRule.objects.create(format_id="4d5f40e1-b4f3-4406-9adf-38d310254062", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".hdf")

    FormatVersion.objects.create(format_id="9b3f9406-a375-4b66-9081-61a317e68cbf", pronom_id="fmt/1042", description="WordPerfect Graphics 2.0", version="2.0", uuid="de582109-8fd7-46cb-a8bd-847e6a10200d")
    IDRule.objects.filter(command_output=".wpg").delete()

    Format.objects.create(description="Microsoft PRX File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="fe82092a-2d87-4e3a-b4d6-02fa394a261a")
    FormatVersion.objects.create(format_id="fe82092a-2d87-4e3a-b4d6-02fa394a261a", pronom_id="fmt/1043", description="Microsoft PRX", version="None", uuid="9dcf7e6d-3515-431f-8ed0-11711bdd0e7e")
    IDRule.objects.create(format_id="9dcf7e6d-3515-431f-8ed0-11711bdd0e7e", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".prx")

    Format.objects.create(description="AutoShade Rendering Slide", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="9a21e188-c69c-48df-ab83-2698d0c865c5")
    FormatVersion.objects.create(format_id="9a21e188-c69c-48df-ab83-2698d0c865c5", pronom_id="fmt/1044", description="AutoShade RND", version="None", uuid="91ec9c6c-f4b9-46ad-ba4f-955938ef91d7")
    IDRule.objects.create(format_id="91ec9c6c-f4b9-46ad-ba4f-955938ef91d7", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".rnd")

    Format.objects.create(description="Q&A Word Processor Document", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="5c45da5f-3e87-4edd-99bf-1d7a2778d2d8")
    FormatVersion.objects.create(format_id="5c45da5f-3e87-4edd-99bf-1d7a2778d2d8", pronom_id="fmt/1045", description="Q&A Write Word Processor (WP)", version="None", uuid="48284829-4f7c-4b07-a4aa-c6de2e6582b2")

    Format.objects.create(description="Draco File Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="3519dd00-481a-4b8d-90b1-6defe365ac33")
    FormatVersion.objects.create(format_id="3519dd00-481a-4b8d-90b1-6defe365ac33", pronom_id="fmt/1046", description="Draco", version="None", uuid="49b30ffd-9a82-41ee-819d-6349d8b1a0de")
    IDRule.objects.create(format_id="49b30ffd-9a82-41ee-819d-6349d8b1a0de", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".drc")

    FormatVersion.objects.create(format_id="4022207c-7ce2-4ab3-866a-65ca2f68dbf5", pronom_id="fmt/1047", description="Geography Markup Language 3.2", version="3.2", uuid="2be024c8-fbde-4615-ab63-fbc429f2441d")
    IDRule.objects.filter(command_output=".gml").delete()

    Format.objects.create(description="OGR GFS File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="949ca049-a6f7-4190-9b7a-49727e8d09cd")
    FormatVersion.objects.create(format_id="949ca049-a6f7-4190-9b7a-49727e8d09cd", pronom_id="fmt/1048", description="OGR GFS File", version="None", uuid="64b5eece-7416-4d6a-8f68-9a54f1016de4")
    IDRule.objects.create(format_id="64b5eece-7416-4d6a-8f68-9a54f1016de4", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".gfs")

    Format.objects.create(description="QuickDraw 3D Metafile (ASCII)", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="bbbe0611-0c38-4567-9bcf-30cb746bde84")
    FormatVersion.objects.create(format_id="bbbe0611-0c38-4567-9bcf-30cb746bde84", pronom_id="fmt/1049", description="3DMF ASCII", version="None", uuid="530dab1c-71cc-4e3e-82de-9786396178e6")
    IDRule.objects.create(format_id="530dab1c-71cc-4e3e-82de-9786396178e6", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".3dmf")

    Format.objects.create(description="QuickDraw 3D Metafile (Binary)", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="8878c629-2c22-44a0-ab2e-03c4addaf178")
    FormatVersion.objects.create(format_id="8878c629-2c22-44a0-ab2e-03c4addaf178", pronom_id="fmt/1050", description="3DMF Binary", version="1", uuid="bf8ad7dc-9587-4a73-879a-325cb170ca4e")
    IDRule.objects.filter(command_output=".3dmf").delete()

    Format.objects.create(description="Windows Journal Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="30dd63f1-9974-42c2-8e22-1bc3d782360a")
    FormatVersion.objects.create(format_id="30dd63f1-9974-42c2-8e22-1bc3d782360a", pronom_id="fmt/1051", description="Windows Journal", version="None", uuid="3c1ca25d-9483-47eb-bee7-be77a2531f05")
    IDRule.objects.create(format_id="3c1ca25d-9483-47eb-bee7-be77a2531f05", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".jnt")

    Format.objects.create(description="BKNAS Seismic Data Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="57809984-fdd4-4b8a-a45f-8b12d4016a93")
    FormatVersion.objects.create(format_id="57809984-fdd4-4b8a-a45f-8b12d4016a93", pronom_id="fmt/1052", description="BKNAS", version="1.0", uuid="6e1c1b1c-0a59-411f-8ca2-02cd722f85c6")
    IDRule.objects.create(format_id="6e1c1b1c-0a59-411f-8ca2-02cd722f85c6", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".bknas")

    Format.objects.create(description="Adobe Audio Waveform", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="6d66819a-6ad7-4f6e-a96d-95d319bf038a")
    FormatVersion.objects.create(format_id="6d66819a-6ad7-4f6e-a96d-95d319bf038a", pronom_id="fmt/1053", description="Adobe .pek", version="None", uuid="1d4252aa-a017-4eab-a3dc-7d7a1efc7921")
    IDRule.objects.create(format_id="1d4252aa-a017-4eab-a3dc-7d7a1efc7921", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".pek")

    Format.objects.create(description="AVCHD Clip Information File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="c45fc923-2743-41ad-8fb1-703533ee04fa")
    FormatVersion.objects.create(format_id="c45fc923-2743-41ad-8fb1-703533ee04fa", pronom_id="fmt/1054", description="AVCHD Clip Information File", version="None", uuid="818804da-7c42-4e2d-a1d1-9042c79c5346")
    IDRule.objects.filter(command_output=".cpi").delete()

    Format.objects.create(description="M2TS", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="9d2f5dcd-ccc3-4e54-b9eb-38682b3d29d7")
    FormatVersion.objects.create(format_id="9d2f5dcd-ccc3-4e54-b9eb-38682b3d29d7", pronom_id="fmt/1055", description="M2TS", version="None", uuid="d17f8df7-c483-46ff-adef-acca7e517a01")
    IDRule.objects.create(format_id="d17f8df7-c483-46ff-adef-acca7e517a01", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".mts")

    Format.objects.create(description="SNAP Main Data File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="94a005c2-8437-4d9f-adb3-c65d7b968a66")
    FormatVersion.objects.create(format_id="94a005c2-8437-4d9f-adb3-c65d7b968a66", pronom_id="fmt/1056", description="SNAP Main data file", version="None", uuid="4b42b267-ea90-458d-a8b0-592a79fad09b")
    IDRule.objects.create(format_id="4b42b267-ea90-458d-a8b0-592a79fad09b", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".mdf")

    Format.objects.create(description="SNAP Archive Data File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="374cffbe-7bc8-4fc7-b96b-68b53b422651")
    FormatVersion.objects.create(format_id="374cffbe-7bc8-4fc7-b96b-68b53b422651", pronom_id="fmt/1057", description="SNAP Archive data file", version="None", uuid="e674a753-8842-4fab-8bf4-e4fcc38fa1b8")
    IDRule.objects.filter(command_output=".adf").delete()

    Format.objects.create(description="SNAP Processed Data File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="a960c6dc-8959-4de9-b14d-92eb540dd963")
    FormatVersion.objects.create(format_id="a960c6dc-8959-4de9-b14d-92eb540dd963", pronom_id="fmt/1058", description="SNAP Processed data file", version="None", uuid="dffcb406-401f-4f29-902e-b2d94884b71a")
    IDRule.objects.create(format_id="dffcb406-401f-4f29-902e-b2d94884b71a", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".snpdf")

    FormatVersion.objects.create(format_id="37904504-22a0-40b2-9505-21f89382d484", pronom_id="fmt/1059", description="FileMaker Pro 2", version="2", uuid="013ec7bb-61d2-425d-b1c7-6fd4e1c49ae2")
    IDRule.objects.filter(command_output=".fm").delete()

    Format.objects.create(description="Phase One Raw Image", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="35692ae4-ae93-41dd-82d9-476b8e38dd49")
    FormatVersion.objects.create(format_id="35692ae4-ae93-41dd-82d9-476b8e38dd49", pronom_id="fmt/1060", description="Phase One Raw big endian", version="None", uuid="41d64274-677f-4a9c-a9cc-8972e23dd846")
    IDRule.objects.filter(command_output=".cap").delete()

    Format.objects.create(description="Phase One IIQ Raw Image", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="53cd1ce7-610e-4b2e-89c2-4a42c302fc20")
    FormatVersion.objects.create(format_id="53cd1ce7-610e-4b2e-89c2-4a42c302fc20", pronom_id="fmt/1061", description="Phase One IIQ Raw", version="None", uuid="9eb7232f-992d-40af-9596-ff574aa26394")
    IDRule.objects.create(format_id="9eb7232f-992d-40af-9596-ff574aa26394", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".iiq")

    Format.objects.create(description="Hasselblad 3FR Raw Image", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="757a61e0-b82d-4a24-b765-36f6dcd01cda")
    FormatVersion.objects.create(format_id="757a61e0-b82d-4a24-b765-36f6dcd01cda", pronom_id="fmt/1062", description="Hasselblad 3FR", version="None", uuid="bc808b74-7c2d-4f02-9bcf-dd8fc600e6fa")
    IDRule.objects.filter(command_output=".3fr").delete()

    Format.objects.create(description="Leaf Mosaic Raw Image", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="9c6e2f60-6ed1-442c-9a2b-befed38ea22b")
    FormatVersion.objects.create(format_id="9c6e2f60-6ed1-442c-9a2b-befed38ea22b", pronom_id="fmt/1063", description="Leaf Mosaic Raw", version="None", uuid="74017184-a319-4223-b0bb-456839a68f08")
    IDRule.objects.create(format_id="74017184-a319-4223-b0bb-456839a68f08", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".mos")

    Format.objects.create(description="Portable Database", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="58393f57-f266-4ba5-83ab-8f1d0fe3f2a7")
    FormatVersion.objects.create(format_id="58393f57-f266-4ba5-83ab-8f1d0fe3f2a7", pronom_id="fmt/1064", description="Portable Database 1", version="1", uuid="1f0aa422-4413-46ed-a62e-6c9af73937a3")
    IDRule.objects.filter(command_output=".pdb").delete()

    FormatVersion.objects.create(format_id="58393f57-f266-4ba5-83ab-8f1d0fe3f2a7", pronom_id="fmt/1065", description="Portable Database 2", version="2", uuid="671a6178-3e1b-45ec-aa58-49cf76f33eb9")
    IDRule.objects.create(format_id="671a6178-3e1b-45ec-aa58-49cf76f33eb9", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".pdb")

    FormatVersion.objects.create(format_id="58393f57-f266-4ba5-83ab-8f1d0fe3f2a7", pronom_id="fmt/1066", description="Portable Database 3", version="3", uuid="78cf6108-c121-4674-9cc3-7089c80fe95e")
    IDRule.objects.filter(command_output=".pdb").delete()

    Format.objects.create(description="Silo", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="a6d8f765-9fe0-4ea9-ab1c-b6eee4894573")
    FormatVersion.objects.create(format_id="a6d8f765-9fe0-4ea9-ab1c-b6eee4894573", pronom_id="fmt/1067", description="SILO PDB 1", version="", uuid="823c7007-57bc-40df-b98a-e699c9bc8f3a")
    IDRule.objects.create(format_id="823c7007-57bc-40df-b98a-e699c9bc8f3a", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".silo")

    FormatVersion.objects.create(format_id="a6d8f765-9fe0-4ea9-ab1c-b6eee4894573", pronom_id="fmt/1068", description="SILO HDF5", version="", uuid="6ba2ec28-2c04-4317-a17a-e5320baa381d")
    IDRule.objects.filter(command_output=".silo").delete()

    Format.objects.create(description="Cue Sheet", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="1d1cc0ba-0624-44a7-be2e-bd0e343be84c")
    FormatVersion.objects.create(format_id="1d1cc0ba-0624-44a7-be2e-bd0e343be84c", pronom_id="fmt/1069", description="CUE Sheet", version="None", uuid="e1896e80-b8b7-452d-8ae0-ff36a584ba54")
    IDRule.objects.create(format_id="e1896e80-b8b7-452d-8ae0-ff36a584ba54", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".cue")

    Format.objects.create(description="Preferred Executable Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="38f38ac3-c985-4864-974d-0ed239ec3fc6")
    FormatVersion.objects.create(format_id="38f38ac3-c985-4864-974d-0ed239ec3fc6", pronom_id="fmt/1070", description="Preferred Executable Format", version="None", uuid="82b3fb83-5534-47d3-a3a6-f7814a5ae175")

    Format.objects.create(description="Apple Disk Image", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="335e1b35-ecb2-44a7-8ed1-dd0acf329673")
    FormatVersion.objects.create(format_id="335e1b35-ecb2-44a7-8ed1-dd0acf329673", pronom_id="fmt/1071", description="Apple Disk Image", version="None", uuid="35ce1ee7-9d72-47ae-b92a-745661df1ef8")
    IDRule.objects.filter(command_output=".dmg").delete()

    FormatVersion.objects.create(format_id="37904504-22a0-40b2-9505-21f89382d484", pronom_id="fmt/1072", description="FileMaker Pro 1", version="1", uuid="38f1c4c9-312f-4062-9543-f073e1d7ef70")

    Format.objects.create(description="Google Document Link File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="545dac6f-60cc-4325-b161-b5c49fb9d22d")
    FormatVersion.objects.create(format_id="545dac6f-60cc-4325-b161-b5c49fb9d22d", pronom_id="fmt/1073", description="Google Document Link File", version="None", uuid="a9a9d3db-6691-45ec-8a0a-a36dbed93f02")
    IDRule.objects.create(format_id="a9a9d3db-6691-45ec-8a0a-a36dbed93f02", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".gslides")

    Format.objects.create(description="AVCHD Playlist File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="a92cb474-bc96-46f8-9a9f-076d1c59e96c")
    FormatVersion.objects.create(format_id="a92cb474-bc96-46f8-9a9f-076d1c59e96c", pronom_id="fmt/1074", description="AVCHD Playlist File 1", version="None", uuid="0c99d4b2-e4b1-4ebe-8ebd-b751be979ee8")
    IDRule.objects.create(format_id="0c99d4b2-e4b1-4ebe-8ebd-b751be979ee8", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".mpl")

    Format.objects.create(description="AVCHD Movie Object File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="8bf48c82-0970-488a-88de-f4aa7cfee94e")
    FormatVersion.objects.create(format_id="8bf48c82-0970-488a-88de-f4aa7cfee94e", pronom_id="fmt/1075", description="AVCHD Movie Object File", version="None", uuid="3bc6345f-6f80-4149-8e1a-697ba68d0207")
    IDRule.objects.create(format_id="3bc6345f-6f80-4149-8e1a-697ba68d0207", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".bdm")

    Format.objects.create(description="AVCHD Index File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="e6377fa8-eb0c-41f7-85e9-d8eda731e717")
    FormatVersion.objects.create(format_id="e6377fa8-eb0c-41f7-85e9-d8eda731e717", pronom_id="fmt/1076", description="AVCHD Index File", version="None", uuid="ba8edd84-f579-4315-98f3-ddec0675b950")
    IDRule.objects.filter(command_output=".bdm").delete()

    Format.objects.create(description="AVCHD Thumbnail Index File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="e0e6764c-616e-44da-9a5e-a5162c1eb641")
    FormatVersion.objects.create(format_id="e0e6764c-616e-44da-9a5e-a5162c1eb641", pronom_id="fmt/1077", description="AVCHD Thumbnail Index File", version="None", uuid="3ed05b73-e60d-41d0-8334-f74b54368740")
    IDRule.objects.create(format_id="3ed05b73-e60d-41d0-8334-f74b54368740", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".tid")

    Format.objects.create(description="Microsoft Program Database", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="233ea0bf-4b04-4cbc-b3d4-fd9b37504de8")
    FormatVersion.objects.create(format_id="233ea0bf-4b04-4cbc-b3d4-fd9b37504de8", pronom_id="fmt/1078", description="Microsoft PDB 2.00", version="2.00", uuid="243e4dfc-dcf2-44d9-bb49-ee7099f74476")
    IDRule.objects.create(format_id="243e4dfc-dcf2-44d9-bb49-ee7099f74476", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".pdb")

    FormatVersion.objects.create(format_id="233ea0bf-4b04-4cbc-b3d4-fd9b37504de8", pronom_id="fmt/1079", description="Microsoft PDB 7.00", version="7.00", uuid="0e7bf332-0b03-4adc-819d-73f9ac489c07")
    IDRule.objects.filter(command_output=".pdb").delete()

    Format.objects.create(description="ASP Application Directive File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="1537816a-27d6-4571-80f0-60cbf554b911")
    FormatVersion.objects.create(format_id="1537816a-27d6-4571-80f0-60cbf554b911", pronom_id="fmt/1080", description="ASP Application Directive", version="None", uuid="3ac12571-040d-40cc-a47c-d988fb0a8ee1")
    IDRule.objects.create(format_id="3ac12571-040d-40cc-a47c-d988fb0a8ee1", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".asax")

    Format.objects.create(description="ASP Control Directive File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="cc36487f-a23d-4cbb-af02-205a6a2cfe47")
    FormatVersion.objects.create(format_id="cc36487f-a23d-4cbb-af02-205a6a2cfe47", pronom_id="fmt/1081", description="ASP Control Directive", version="None", uuid="7594ca97-8587-4bc1-a818-b08d6be7a813")
    IDRule.objects.create(format_id="7594ca97-8587-4bc1-a818-b08d6be7a813", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".ascx")

    Format.objects.create(description="ASP WebService Directive File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="71748eca-75e8-4810-8b74-b5949692bba7")
    FormatVersion.objects.create(format_id="71748eca-75e8-4810-8b74-b5949692bba7", pronom_id="fmt/1082", description="ASP WebService Directive", version="None", uuid="c49d5a49-4186-4b05-8476-b7c43f0b59b5")
    IDRule.objects.create(format_id="c49d5a49-4186-4b05-8476-b7c43f0b59b5", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".asmx")

    Format.objects.create(description="Hangul Word Processor Document", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="1a91d8c5-7bfb-47b1-9e4c-8dd934f33cda")
    FormatVersion.objects.create(format_id="1a91d8c5-7bfb-47b1-9e4c-8dd934f33cda", pronom_id="fmt/1083", description="HWP 3", version="3", uuid="c14a474d-00b8-45ba-882f-28fc88f5ffbf")
    IDRule.objects.create(format_id="c14a474d-00b8-45ba-882f-28fc88f5ffbf", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".hwp")

    FormatVersion.objects.create(format_id="1a91d8c5-7bfb-47b1-9e4c-8dd934f33cda", pronom_id="fmt/1084", description="Hangul Word Processor Document", version="5", uuid="6aad4402-39d6-45d7-9f74-baf2a8d2a27b")
    IDRule.objects.filter(command_output=".hwp").delete()

    Format.objects.create(description="TRIM Context Reference File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="6f792e7f-0e96-4d87-9588-85e14fd4d25e")
    FormatVersion.objects.create(format_id="6f792e7f-0e96-4d87-9588-85e14fd4d25e", pronom_id="fmt/1085", description="TRIM Context Reference File", version="None", uuid="97db2e67-c375-44de-8075-c7b7dd69f4c8")
    IDRule.objects.create(format_id="97db2e67-c375-44de-8075-c7b7dd69f4c8", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".tr5")

    Format.objects.create(description="Monkey's Audio File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="cebeecd6-ce04-46c3-af92-43e3a4d08ca2")
    FormatVersion.objects.create(format_id="cebeecd6-ce04-46c3-af92-43e3a4d08ca2", pronom_id="fmt/1086", description="Monkey's Audio variant 1", version="None", uuid="87ed7ce6-cbca-4e38-8eaa-f31a70f337c0")
    IDRule.objects.create(format_id="87ed7ce6-cbca-4e38-8eaa-f31a70f337c0", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".ape")

    Format.objects.create(description="FAT Disk Image", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="576a0e0b-a01f-4bec-bd28-8b21105fe07b")
    FormatVersion.objects.create(format_id="576a0e0b-a01f-4bec-bd28-8b21105fe07b", pronom_id="fmt/1087", description="FAT Disk Image", version="None", uuid="ffdad5e7-c536-4e8e-b186-045ab129b61c")
    IDRule.objects.filter(command_output=".img").delete()

    Format.objects.create(description="Visual Basic (VB) File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="dfe40dbb-5a58-45c3-bc5a-f5533161e1f9")
    FormatVersion.objects.create(format_id="dfe40dbb-5a58-45c3-bc5a-f5533161e1f9", pronom_id="fmt/1088", description="Visual Basic (VB) File", version="None", uuid="9a362fb0-27bd-406c-8d45-ab62a7f018af")
    IDRule.objects.create(format_id="9a362fb0-27bd-406c-8d45-ab62a7f018af", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".vb")

    Format.objects.create(description="VBScript (VBS) File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="7362fe48-3f60-4185-82b6-ea28de54f6d2")
    FormatVersion.objects.create(format_id="7362fe48-3f60-4185-82b6-ea28de54f6d2", pronom_id="fmt/1089", description="VBScript (VBS) File", version="None", uuid="873efec2-3616-47d8-81b6-ae0b745fb648")
    IDRule.objects.create(format_id="873efec2-3616-47d8-81b6-ae0b745fb648", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".vbs")

    Format.objects.create(description="Exclude File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="3be95ba5-581f-4002-924b-18b502e2a5f1")
    FormatVersion.objects.create(format_id="3be95ba5-581f-4002-924b-18b502e2a5f1", pronom_id="fmt/1090", description="Exclude File", version="None", uuid="4df221f1-e628-48c4-be93-c5f94ca1470d")
    IDRule.objects.create(format_id="4df221f1-e628-48c4-be93-c5f94ca1470d", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".exclude")

    Format.objects.create(description="Scribus Document", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="cfc197b4-c039-4ea3-9fc2-d7cdbaa53140")
    FormatVersion.objects.create(format_id="cfc197b4-c039-4ea3-9fc2-d7cdbaa53140", pronom_id="fmt/1091", description="Scribus", version="None", uuid="a2a506d3-55ed-4865-9c24-14a9a9df57d8")
    IDRule.objects.create(format_id="a2a506d3-55ed-4865-9c24-14a9a9df57d8", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".sla")

    Format.objects.create(description="Alias Pix Image File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="e86fab63-2d29-4035-a11f-1f5b9aaaf5a9")
    FormatVersion.objects.create(format_id="e86fab63-2d29-4035-a11f-1f5b9aaaf5a9", pronom_id="fmt/1092", description="Alias Pix Image", version="None", uuid="9ad3ebc4-a3a1-4d52-aa2e-272add00e5af")
    IDRule.objects.filter(command_output=".pix").delete()

    Format.objects.create(description="Alias Scene Description Language", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="cb51a1dc-3fd7-4ebe-90b1-e1bbecca7ee7")
    FormatVersion.objects.create(format_id="cb51a1dc-3fd7-4ebe-90b1-e1bbecca7ee7", pronom_id="fmt/1093", description="Alias Scene Description Language", version="None", uuid="c306ba16-4692-4d7b-ba91-89e4edc829a1")
    IDRule.objects.create(format_id="c306ba16-4692-4d7b-ba91-89e4edc829a1", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".sdl")

    Format.objects.create(description="The Neuroimaging Informatics Technology Initiative File Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="42b7510a-e4af-4a76-8702-d3eb9910e8dd")
    FormatVersion.objects.create(format_id="42b7510a-e4af-4a76-8702-d3eb9910e8dd", pronom_id="fmt/1094", description="The Neuroimaging Informatics Technology Initiative File Format V2 variant1", version="2", uuid="0f846e4c-8dc6-445b-b0a1-edd4f1c7f4be")
    IDRule.objects.create(format_id="0f846e4c-8dc6-445b-b0a1-edd4f1c7f4be", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".nii")

    Format.objects.create(description="PEA Archive Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="f18c7e97-f753-404a-9669-266193f82d0d")
    FormatVersion.objects.create(format_id="f18c7e97-f753-404a-9669-266193f82d0d", pronom_id="fmt/1095", description="PEA Archive", version="None", uuid="7ac94685-cf1a-41e7-a27e-8a4fa095eff9")
    IDRule.objects.create(format_id="7ac94685-cf1a-41e7-a27e-8a4fa095eff9", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".pea")

    Format.objects.create(description="FreeArc Archive Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="c6f71d37-39a3-4112-a0bd-4e19eeda8cdd")
    FormatVersion.objects.create(format_id="c6f71d37-39a3-4112-a0bd-4e19eeda8cdd", pronom_id="fmt/1096", description="FreeArc Archive Format", version="None", uuid="557d808a-5eb6-424d-bb9d-b7642383606c")
    IDRule.objects.filter(command_output=".arc").delete()

    Format.objects.create(description="ZPAQ Archive Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="39d287c8-f55e-4a41-8f5c-c48452cc1d9b")
    FormatVersion.objects.create(format_id="39d287c8-f55e-4a41-8f5c-c48452cc1d9b", pronom_id="fmt/1097", description="ZPAQ Archive Format variant 1", version="None", uuid="3a23dfa5-40e3-4e6b-9181-dc6f97a7736a")
    IDRule.objects.create(format_id="3a23dfa5-40e3-4e6b-9181-dc6f97a7736a", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".zpaq")

    Format.objects.create(description="TCR eBook", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="47628c18-73ab-4086-9c87-d1e0b107f80f")
    FormatVersion.objects.create(format_id="47628c18-73ab-4086-9c87-d1e0b107f80f", pronom_id="fmt/1099", description="TCR eBook", version="None", uuid="77fab12d-e8eb-402d-861f-6cee88816648")
    IDRule.objects.create(format_id="77fab12d-e8eb-402d-861f-6cee88816648", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".tcr")

    Format.objects.create(description="XZ File Format", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="5f1ab6e3-33ff-43da-a491-45cd83fff57a")
    FormatVersion.objects.create(format_id="5f1ab6e3-33ff-43da-a491-45cd83fff57a", pronom_id="fmt/1098", description="XZ File Format", version="None", uuid="b2f87a44-d7eb-4d50-be59-c627c5ad5243")
    IDRule.objects.create(format_id="b2f87a44-d7eb-4d50-be59-c627c5ad5243", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".xz")

    Format.objects.create(description="yEnc Encoded File", group_id="00abbdd0-51b3-4162-b93a-45deb4ed8654", uuid="ff257a80-d2ae-49e0-8a69-1bb3544e46ec")
    FormatVersion.objects.create(format_id="ff257a80-d2ae-49e0-8a69-1bb3544e46ec", pronom_id="fmt/1100", description="yEnc File", version="None", uuid="798e8a89-1e2f-4152-bad1-0940e7e48c2f")
    IDRule.objects.create(format_id="798e8a89-1e2f-4152-bad1-0940e7e48c2f", command_id="41efbe1b-3fc7-4b24-9290-d0fb5d0ea9e9", command_output=".yenc")


class Migration(migrations.Migration):

    dependencies = [
        ('fpr', '0014_fix_fits_command'),
    ]

    operations = [
        migrations.RunPython(data_migration),
    ]
