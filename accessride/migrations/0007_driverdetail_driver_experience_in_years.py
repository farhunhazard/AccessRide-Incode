# Generated by Django 4.2.2 on 2023-07-07 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessride', '0006_detail_mode_of_ride'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverdetail',
            name='driver_experience_in_years',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
