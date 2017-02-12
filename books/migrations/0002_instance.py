# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CloundPlatform', models.CharField(max_length=20)),
                ('IpAddress', models.GenericIPAddressField()),
                ('Note', models.CharField(max_length=140)),
                ('CPUINumber', models.PositiveSmallIntegerField()),
                ('CPUCoreNumber', models.PositiveSmallIntegerField()),
                ('CPUMhz', models.PositiveSmallIntegerField()),
                ('MemInfo', models.PositiveIntegerField()),
                ('DiskInfo', models.PositiveIntegerField()),
                ('Bandwidth', models.PositiveSmallIntegerField()),
                ('Price', models.PositiveIntegerField()),
                ('TimeLeft', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
