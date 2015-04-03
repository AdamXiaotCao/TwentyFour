# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twentyFour', '0025_auto_20141206_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='total_points',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='card_sets',
            field=models.ManyToManyField(to=b'twentyFour.Cardset'),
        ),
    ]
