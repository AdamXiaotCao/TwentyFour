# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twentyFour', '0002_auto_20141123_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='card_sets',
            field=models.ManyToManyField(to=b'twentyFour.Cardset'),
        ),
    ]
