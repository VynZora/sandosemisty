# Generated by Django 5.2 on 2025-05-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "sandose_misty_app",
            "0002_roomprice_room_type_alter_roomprice_price_per_night",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomprice",
            name="room_type",
            field=models.CharField(
                choices=[("Deluxe", "Deluxe Room"), ("Suite", "Suite Room")],
                max_length=50,
            ),
        ),
    ]
