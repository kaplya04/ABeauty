# Generated by Django 5.0.4 on 2024-06-18 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appab', '0029_remove_rating_product_remove_rating_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar',
            name='rating',
        ),
        migrations.AddField(
            model_name='modal',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
