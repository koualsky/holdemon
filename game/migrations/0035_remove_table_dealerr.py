# Generated by Django 2.2.4 on 2019-08-07 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0034_table_dealerr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='dealerr',
        ),
    ]
