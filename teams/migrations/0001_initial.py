# Generated by Django 4.0.2 on 2022-02-09 01:01

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("kits", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("fpl_id", models.IntegerField(unique=True)),
                ("name", models.CharField(max_length=128, unique=True)),
                ("short_name", models.CharField(max_length=10, unique=True)),
                ("strength_attack_home", models.IntegerField(default=0)),
                ("strength_attack_away", models.IntegerField(default=0)),
                ("strength_defence_home", models.IntegerField(default=0)),
                ("strength_defence_away", models.IntegerField(default=0)),
                (
                    "kit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teams",
                        to="kits.kit",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
