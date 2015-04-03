# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twentyFour', '0017_auto_20141123_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='card_sets',
            field=models.ManyToManyField(to=b'twentyFour.Cardset'),
        ),
    ]
