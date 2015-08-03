# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user_stories', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(db_index=True, serialize=False, primary_key=True)),
                ('task_name', models.CharField(max_length=50)),
                ('task_description', models.CharField(max_length=250)),
                ('task_status', models.CharField(default=b'To-Do', max_length=20)),
                ('story', models.ForeignKey(to='user_stories.UserStory', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
