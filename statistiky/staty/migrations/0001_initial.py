# Generated by Django 3.2 on 2021-05-02 07:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Druh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oznaceni_druhu', models.CharField(help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný', max_length=50, unique=True, verbose_name='Označení druhu zboží')),
                ('oblast', models.CharField(blank=True, default='Centr', help_text='Vyberte označení oblasti', max_length=40, verbose_name='Oblast')),
            ],
            options={
                'verbose_name': 'Druh zboží',
                'verbose_name_plural': 'Druh zboží',
                'ordering': ['oznaceni_druhu'],
            },
        ),
        migrations.CreateModel(
            name='Statistiky',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(help_text='Zadejte jméno maximální délce 30 znaků', max_length=30, verbose_name='Jméno Hráče')),
                ('prijmeni', models.CharField(help_text='Zadejte příjmení maximální délce 30 znaků', max_length=30, verbose_name='Příjmení Hráče')),
                ('popis', models.TextField(blank=True, null=True, verbose_name='Rychlý životopis')),
                ('vyplata', models.IntegerField(help_text='Zadejte nezáporné číslo', null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Výplata')),
                ('kvalita', models.IntegerField(blank=True, choices=[(10, '10'), (9, '9'), (8, '8'), (7, '7'), (6, '6'), (5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')], default=5, help_text='Vyberte označení kvality', verbose_name='Kvalita hráče')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='staty/%Y/%m/%d/', verbose_name='Profilovka')),
                ('druh', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='staty.druh')),
            ],
            options={
                'verbose_name': 'staty',
                'verbose_name_plural': 'staty',
                'ordering': ['prijmeni'],
            },
        ),
    ]
