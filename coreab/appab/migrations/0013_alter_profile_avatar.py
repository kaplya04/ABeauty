# Generated by Django 5.0.4 on 2024-06-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appab', '0012_alter_modal_options_alter_oplata_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]