# Generated by Django 3.0.7 on 2020-07-25 07:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200724_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='updateed_at',
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
