# Generated by Django 5.0.4 on 2024-06-18 15:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appab', '0005_order_procedure_specialist_subscription_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='orders',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='procedure',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='specialist',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subscriptions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='visits',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
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
            name='User',
        ),
        migrations.DeleteModel(
            name='Visit',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
