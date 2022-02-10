# Generated by Django 4.0.2 on 2022-02-10 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0001_initial"),
        ("matches", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="match",
            options={"verbose_name_plural": "Matches"},
        ),
        migrations.AlterUniqueTogether(
            name="match",
            unique_together={("home_team", "away_team")},
        ),
    ]
