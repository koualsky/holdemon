# Generated by Django 2.2.4 on 2019-08-08 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0059_auto_20190808_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='turn',
        ),
    ]
