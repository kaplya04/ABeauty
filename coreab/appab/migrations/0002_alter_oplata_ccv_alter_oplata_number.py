# Generated by Django 5.0.1 on 2024-02-06 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oplata',
            name='ccv',
            field=models.CharField(max_length=300, unique=True, verbose_name='Три цифры'),
        ),
        migrations.AlterField(
            model_name='oplata',
            name='number',
            field=models.CharField(max_length=300, unique=True, verbose_name='Номер карты'),
        ),
    ]
