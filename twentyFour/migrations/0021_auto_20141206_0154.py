# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twentyFour', '0020_auto_20141123_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerstate',
            name='progress',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='value',
            field=models.IntegerField(default=0, max_length=10, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
        migrations.AlterField(
            model_name='game',
            name='card_sets',
            field=models.ManyToManyField(to=b'twentyFour.Cardset'),
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(default=b'WAIT', max_length=8, choices=[(b'WAIT', b'WAIT'), (b'ONGOING', b'ONGOING'), (b'END', b'END')]),
        ),
    ]
