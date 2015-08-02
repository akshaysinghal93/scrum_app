# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum_teams', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserStory',
        ),
        migrations.RemoveField(
            model_name='scrumteam',
            name='id',
        ),
        migrations.AddField(
            model_name='scrumteam',
            name='team_id',
            field=models.AutoField(default=-1, serialize=False, db_index=True, primary_key=True),
            preserve_default=False,
        ),
    ]
