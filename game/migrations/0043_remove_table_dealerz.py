# Generated by Django 2.2.4 on 2019-08-08 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0042_table_dealerz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='dealerz',
        ),
    ]
