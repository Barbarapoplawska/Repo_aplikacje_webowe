# Generated by Django 5.1.1 on 2025-01-24 22:05

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=80)),
                ('opis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=40)),
                ('nazwisko', models.CharField(max_length=60)),
                ('plec', models.IntegerField(choices=[(1, 'Kobieta'), (2, 'Męczyzna'), (3, 'Inne')], default='I')),
                ('data_dodania', models.DateTimeField(default=datetime.date.today)),
                ('stanowisko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folder_aplikacji.stanowisko')),
            ],
            options={
                'ordering': ['nazwisko'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('pseudonim', models.CharField(default='', max_length=80)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='S', max_length=1)),
                ('month_added', models.IntegerField(choices=[(1, 'Styczeń'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecień'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpień'), (9, 'Wrzesień'), (10, 'Październik'), (11, 'Listopad'), (12, 'Grudzień')], default=1)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='folder_aplikacji.team')),
            ],
        ),
    ]
