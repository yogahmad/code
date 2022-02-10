# Generated by Django 4.0.2 on 2022-02-09 02:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
        ('teams', '0001_initial'),
        ('stats', '0004_playerbettingodd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerbettingodd',
            name='number',
        ),
        migrations.AddField(
            model_name='playerbettingodd',
            name='odd',
            field=models.FloatField(default=0.0),
        ),
        migrations.CreateModel(
            name='TeamBettingOdd',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('identifier', models.CharField(choices=[('clean_sheets', 'clean_sheets')], max_length=32)),
                ('odd', models.FloatField(default=0.0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_betting_odds', to='matches.match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_betting_odds', to='teams.team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]