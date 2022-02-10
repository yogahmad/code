# Generated by Django 4.0.2 on 2022-02-10 03:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0002_generatematchdata_alter_generategameweekdata_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenerateTeamData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Generate team data',
            },
        ),
    ]
