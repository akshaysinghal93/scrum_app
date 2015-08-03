# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20150803_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='effort_required',
            field=models.IntegerField(default=10),
        ),
    ]
