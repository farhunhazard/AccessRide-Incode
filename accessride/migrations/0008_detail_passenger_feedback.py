# Generated by Django 4.2.2 on 2023-07-08 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessride', '0007_driverdetail_driver_experience_in_years'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='passenger_feedback',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
