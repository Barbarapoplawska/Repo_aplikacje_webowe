# Generated by Django 5.1.1 on 2025-01-24 22:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
