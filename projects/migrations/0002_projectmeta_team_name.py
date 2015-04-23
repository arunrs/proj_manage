# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmeta',
            name='team_name',
            field=models.CharField(default='sample', max_length=150),
            preserve_default=False,
        ),
    ]
