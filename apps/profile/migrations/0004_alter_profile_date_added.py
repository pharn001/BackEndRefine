# Generated by Django 5.0.7 on 2024-07-12 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_profile_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
