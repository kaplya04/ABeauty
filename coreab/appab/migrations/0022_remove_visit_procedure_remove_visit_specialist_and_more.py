# Generated by Django 5.0.4 on 2024-06-18 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appab', '0021_order_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='procedure',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='specialist',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='users',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Procedure',
        ),
        migrations.DeleteModel(
            name='Specialist',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
        migrations.DeleteModel(
            name='Visit',
        ),
    ]
