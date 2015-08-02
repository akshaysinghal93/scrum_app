# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum_teams', '0002_auto_20150801_1808'),
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='scrum_team',
            field=models.ForeignKey(to='scrum_teams.ScrumTeam', null=True),
        ),
    ]
