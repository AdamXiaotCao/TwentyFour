# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twentyFour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game', models.OneToOneField(to='twentyFour.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayerState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('point', models.IntegerField(default=0)),
                ('gamestate', models.ForeignKey(to='twentyFour.GameState')),
                ('player', models.OneToOneField(to='twentyFour.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='game',
            name='card_sets',
            field=models.ManyToManyField(to=b'twentyFour.Cardset'),
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(default=b'END', max_length=8, choices=[(b'WAIT', b'WAIT'), (b'ONGOING', b'ONGOING'), (b'END', b'END')]),
        ),
    ]
