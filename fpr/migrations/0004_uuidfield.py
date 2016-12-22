# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fpr.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fpr', '0003_pronom_84'),
    ]

    operations = [
        migrations.AlterField(
            model_name='format',
            name='uuid',
            field=fpr.models.DefaultUUIDField(default=uuid.uuid4, help_text=b'Unique identifier', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='formatgroup',
            name='uuid',
            field=fpr.models.DefaultUUIDField(default=uuid.uuid4, help_text=b'Unique identifier', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='formatversion',
            name='uuid',
            field=fpr.models.DefaultUUIDField(default=uuid.uuid4, help_text=b'Unique identifier', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='fpcommand',
            name='uuid',
            field=fpr.models.DefaultUUIDField(default=uuid.uuid4, help_text=b'Unique identifier', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='fprule',
            name='uuid',
            field=fpr.models.DefaultUUIDField(default=uuid.uuid4, help_text=b'Unique identifier', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='fptool',
            name='uuid',
            field=fpr.models.DefaultUUIDField(default=uuid.uuid4, help_text=b'Unique identifier', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='idcommand',
            name='uuid',
            field=fpr.models.DefaultUUIDField(default=uuid.uuid4, help_text=b'Unique identifier', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='idrule',
            name='uuid',
            field=fpr.models.DefaultUUIDField(default=uuid.uuid4, help_text=b'Unique identifier', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='idtool',
            name='uuid',
            field=fpr.models.DefaultUUIDField(default=uuid.uuid4, help_text=b'Unique identifier', unique=True, editable=False),
        ),
    ]
