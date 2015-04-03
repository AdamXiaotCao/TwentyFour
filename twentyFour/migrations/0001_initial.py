# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(default=-1, max_length=10, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CardSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cards', models.ManyToManyField(to='twentyFour.Card')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('card_sets', models.ManyToManyField(to='twentyFour.CardSet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_games_played', models.IntegerField(default=0)),
                ('total_games_won', models.IntegerField(default=0)),
                ('picture', models.ImageField(default=b'/media/user-photos/default.jpg', upload_to=b'user-photos')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('win', models.BooleanField(default=False)),
                ('game_played', models.OneToOneField(to='twentyFour.Game')),
                ('player', models.ForeignKey(to='twentyFour.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='participants',
            field=models.ManyToManyField(to='twentyFour.Player'),
            preserve_default=True,
        ),
    ]
