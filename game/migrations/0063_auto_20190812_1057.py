# Generated by Django 2.2.4 on 2019-08-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0062_auto_20190808_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='cards',
            field=models.CharField(max_length=100, null=True),
        ),
    ]