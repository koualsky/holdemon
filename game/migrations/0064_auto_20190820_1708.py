# Generated by Django 2.2.4 on 2019-08-20 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0063_auto_20190812_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='username',
        ),
    ]
