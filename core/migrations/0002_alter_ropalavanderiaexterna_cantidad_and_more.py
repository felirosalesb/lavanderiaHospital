# Generated by Django 5.0.6 on 2024-11-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ropalavanderiaexterna",
            name="cantidad",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="ropalavanderiahospital",
            name="cantidad",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]