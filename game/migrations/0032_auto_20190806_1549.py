# Generated by Django 2.2.4 on 2019-08-06 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0031_auto_20190806_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='dealer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dealer', to='game.Player'),
        ),
    ]
