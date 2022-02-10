# Generated by Django 4.0.2 on 2022-02-10 03:30

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scripts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GenerateMatchData",
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
            ],
            options={
                "verbose_name_plural": "Generate match data",
            },
        ),
        migrations.AlterModelOptions(
            name="generategameweekdata",
            options={"verbose_name_plural": "Generate gameweek data"},
        ),
    ]
