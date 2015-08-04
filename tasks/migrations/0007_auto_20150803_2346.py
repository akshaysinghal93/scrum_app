# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_effort_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='effort_required',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(max_length=20),
        ),
    ]
