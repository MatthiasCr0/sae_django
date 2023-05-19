# Generated by Django 4.1.7 on 2023-05-19 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0014_alter_machine_maintenancedate_alter_machine_vlan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 19, 11, 30, 45, 428868)
            ),
        ),
        migrations.AlterField(
            model_name="machine",
            name="vlan",
            field=models.CharField(
                choices=[("Gestion", "77"), ("Clients", "10"), ("Services", "20")],
                default="Gestion",
                max_length=32,
            ),
        ),
    ]