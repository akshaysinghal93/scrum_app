# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrumTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(default=b'Default', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('story_id', models.AutoField(db_index=True, serialize=False, primary_key=True)),
                ('story_ref', models.CharField(unique=True, max_length=10)),
                ('story_title', models.CharField(max_length=200)),
                ('story_desc', models.CharField(max_length=1000)),
                ('effort_required', models.IntegerField()),
            ],
        ),
    ]
