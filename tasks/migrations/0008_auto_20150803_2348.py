# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20150803_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='effort_required',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(default=b'To-Do', max_length=20),
        ),
    ]
