# Generated by Django 5.0.7 on 2024-07-12 06:18

import sorl.thumbnail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='image/brand', verbose_name='Brand')),
                ('is_popular', models.BooleanField(default=False)),
            ],
        ),
    ]