# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20150803_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='story',
            field=models.ForeignKey(null=True, blank=True, to='user_stories.UserStory'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
