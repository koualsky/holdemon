# Generated by Django 2.2.4 on 2019-08-05 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0016_auto_20190805_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='table',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='table', to='game.Table'),
        ),
    ]
