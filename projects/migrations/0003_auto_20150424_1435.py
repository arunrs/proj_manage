# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projectmeta_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='status',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'New'), ('O', 'Open'), ('C', 'Closed')]),
        ),
        migrations.AddField(
            model_name='bug',
            name='types',
            field=models.CharField(max_length=1, default='C', choices=[('C', 'Current'), ('E', 'Enhancement')]),
        ),
        migrations.AddField(
            model_name='task',
            name='reopened',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'New'), ('O', 'Open'), ('C', 'Closed')]),
        ),
        migrations.AddField(
            model_name='task',
            name='types',
            field=models.CharField(max_length=1, default='C', choices=[('C', 'Current'), ('E', 'Enhancement')]),
        ),
    ]
