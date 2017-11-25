# -*- coding: utf-8 -*-

from django.test import TestCase

from fpr.models import (
    Format,
    FormatGroup,
    FormatVersion,
    IDTool,
    FPTool,
)

STR_GT_50CH = 'Lorem ipsum dolor sit amet, consectetur adipiscing elitam.'
STR_GT_50CH_SLUG_1 = 'lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-'
STR_GT_50CH_SLUG_2 = 'lorem-ipsum-dolor-sit-amet-consectetur-adipiscin-2'

STR_EQ_50CH = 'Lorem ipsum dolor sit amet, consectetur fand elitam.'
STR_EQ_50CH_SLUG_1 = 'lorem-ipsum-dolor-sit-amet-consectetur-fand-elitam'
STR_EQ_50CH_SLUG_2 = 'lorem-ipsum-dolor-sit-amet-consectetur-fand-elit-2'

STR_LT_50CH = 'Lorem ipsum dolor sit amet, fand elit.'
STR_LT_50CH_SLUG_1 = 'lorem-ipsum-dolor-sit-amet-fand-elit'
STR_LT_50CH_SLUG_2 = 'lorem-ipsum-dolor-sit-amet-fand-elit-2'


class AutoSlugFieldsTest(TestCase):

    def run_basic_length_tests_against_model(self, model, field):
        obj = model.objects.create(**{field: STR_GT_50CH})
        self.assertEqual(obj.slug, STR_GT_50CH_SLUG_1)
        self.assertLessEqual(
            len(obj.slug),
            Format._meta.get_field('slug').max_length)

        obj = model.objects.create(**{field: STR_GT_50CH})
        self.assertEqual(obj.slug, STR_GT_50CH_SLUG_2)

        obj = Format.objects.create(**{field: STR_EQ_50CH})
        self.assertEqual(obj.slug, STR_EQ_50CH_SLUG_1)

        obj = Format.objects.create(**{field: STR_EQ_50CH})
        self.assertEqual(obj.slug, STR_EQ_50CH_SLUG_2)

        obj = Format.objects.create(**{field: STR_LT_50CH})
        self.assertEqual(obj.slug, STR_LT_50CH_SLUG_1)

        obj = Format.objects.create(**{field: STR_LT_50CH})
        self.assertEqual(obj.slug, STR_LT_50CH_SLUG_2)

    def test_format_group_slug_field(self):
        self.run_basic_length_tests_against_model(FormatGroup, 'description')

    def test_format_slug_field(self):
        self.run_basic_length_tests_against_model(Format, 'description')

    def test_format_version_slug_field(self):
        fmt1 = Format.objects.create(description='My format A')
        fmt2 = Format.objects.create(description='My format B')
        obj1 = FormatVersion.objects.create(format=fmt1, description='FormatV')
        obj2 = FormatVersion.objects.create(format=fmt2, description='FormatV')
        obj3 = FormatVersion.objects.create(format=fmt2, description='FormatV')

        self.assertEqual(fmt1.slug, 'my-format-a')
        self.assertEqual(fmt2.slug, 'my-format-b')
        self.assertEqual(obj1.slug, 'formatv')
        self.assertEqual(obj2.slug, 'formatv')
        self.assertEqual(obj3.slug, 'formatv-2')

        obj3.description = 'New description'
        obj3.save()
        self.assertEqual(obj3.slug, 'new-description')

    def test_idtool_slug_field(self):
        id1 = IDTool.objects.create(description='The Tool', version='3.0.0')
        id2 = IDTool.objects.create(description='The Tool', version='3.0.0')

        self.assertEqual(id1.slug, 'the-tool-300')
        self.assertEqual(id2.slug, 'the-tool-300-2')

        id2.description = 'New description'
        id2.save()
        self.assertEqual(id2.slug, 'new-description-300')

    def test_fptool_slug_field(self):
        id1 = FPTool.objects.create(description='The Tool', version='3.0.0')
        id2 = FPTool.objects.create(description='The Tool', version='3.0.0')

        self.assertEqual(id1.slug, 'the-tool-300')
        self.assertEqual(id2.slug, 'the-tool-300-2')
