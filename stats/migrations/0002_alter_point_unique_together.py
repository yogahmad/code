# Generated by Django 4.0.2 on 2022-02-10 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
        ('players', '0002_alter_player_chance_of_playing_next_round'),
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='point',
            unique_together={('identifier', 'player', 'match')},
        ),
    ]
