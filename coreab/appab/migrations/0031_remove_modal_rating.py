# Generated by Django 5.0.4 on 2024-06-18 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appab', '0030_remove_tovar_rating_modal_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modal',
            name='rating',
        ),
    ]