# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '__first__'),
        ('user_stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='sprint',
            field=models.ForeignKey(to='sprint.Sprint', null=True),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='story_ref',
            field=models.CharField(max_length=10),
        ),
    ]
