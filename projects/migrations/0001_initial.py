# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('actual_end_date', models.DateField(null=True, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('page_url', models.URLField(null=True, blank=True)),
                ('reopened', models.IntegerField(default=0)),
                ('closed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bug',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('model_name', models.CharField(max_length=50)),
                ('reference', models.IntegerField()),
                ('comment', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Domian',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilereferenceModel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('model_name', models.CharField(max_length=50)),
                ('reference', models.IntegerField()),
                ('image_file', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'file_paths',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('actual_end_date', models.DateField(null=True, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('client_name', models.ForeignKey(verbose_name='client_name', related_name='client_name', to=settings.AUTH_USER_MODEL)),
                ('domain', models.ForeignKey(verbose_name='project_domain', related_name='project_domain', to='projects.Domian')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='ProjectMeta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('developer', models.ManyToManyField(verbose_name='project_developer', related_name='project_developer', to=settings.AUTH_USER_MODEL)),
                ('project_watcher', models.ManyToManyField(verbose_name='watchers', related_name='watchers', to=settings.AUTH_USER_MODEL)),
                ('scrum', models.ForeignKey(verbose_name='project_scrum', related_name='project_scrum', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('actual_end_date', models.DateField(null=True, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('version', models.FloatField(default=0.1)),
                ('tagged', models.FloatField(null=True, blank=True)),
                ('freezed_sprint', models.BooleanField(default=True)),
                ('project_ref', models.ForeignKey(verbose_name='project_ref', related_name='project_ref', to='projects.Project')),
            ],
            options={
                'db_table': 'sprint',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('actual_end_date', models.DateField(null=True, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=100)),
                ('slug_name', models.SlugField()),
                ('estimated_hrs', models.PositiveSmallIntegerField(default=1)),
                ('any_delay', models.BooleanField(default=True)),
                ('reason_delay', models.TextField(null=True, blank=True)),
                ('additional', models.BooleanField(default=False)),
                ('closed', models.BooleanField(default=False)),
                ('allocated_user', models.ForeignKey(verbose_name='alloted_dev', related_name='alloted_dev', to=settings.AUTH_USER_MODEL)),
                ('comments', models.ForeignKey(blank=True, null=True, to='projects.CommentModel')),
                ('screeshots', models.ForeignKey(blank=True, null=True, to='projects.FilereferenceModel')),
                ('sprint', models.ForeignKey(verbose_name='sprint_name', related_name='sprint_name', to='projects.Sprint')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='meta',
            field=models.ForeignKey(verbose_name='project_meta', related_name='project_meta', to='projects.ProjectMeta'),
        ),
        migrations.AddField(
            model_name='bug',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, to='projects.CommentModel'),
        ),
        migrations.AddField(
            model_name='bug',
            name='related_task',
            field=models.ForeignKey(blank=True, null=True, to='projects.Task'),
        ),
        migrations.AddField(
            model_name='bug',
            name='screenshot',
            field=models.ForeignKey(blank=True, null=True, to='projects.FilereferenceModel'),
        ),
        migrations.AlterUniqueTogether(
            name='sprint',
            unique_together=set([('project_ref', 'name')]),
        ),
    ]
