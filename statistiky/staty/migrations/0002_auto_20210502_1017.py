# Generated by Django 3.2 on 2021-05-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staty', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='druh',
            options={'ordering': ['oznaceni_druhu'], 'verbose_name': 'Druh hráče', 'verbose_name_plural': 'Druh hráče'},
        ),
        migrations.AlterField(
            model_name='druh',
            name='oblast',
            field=models.CharField(blank=True, choices=[('Levé křídlo', 'Levé křídlo'), ('Pravé křídlo', 'Pravé křídlo'), ('Brankář', 'Brankář'), ('Centr', 'Centr'), ('Obrana', 'Obrana')], default='Centr', help_text='Vyberte označení oblasti', max_length=40, verbose_name='Oblast'),
        ),
        migrations.AlterField(
            model_name='druh',
            name='oznaceni_druhu',
            field=models.CharField(help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný', max_length=50, unique=True, verbose_name='Označení druhu hráče'),
        ),
    ]
