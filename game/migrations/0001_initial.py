# Generated by Django 2.1.2 on 2019-08-29 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=100)),
                ('round_money', models.IntegerField(default=0)),
                ('cards', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(default='out', max_length=100)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool', models.IntegerField(default=0)),
                ('deck', models.CharField(max_length=500, null=True)),
                ('cards_on_table', models.CharField(max_length=100, null=True)),
                ('game_state', models.CharField(default='ready', max_length=200, null=True)),
                ('big_blind', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='big_blind', to='game.Player')),
                ('dealer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dealer', to='game.Player')),
                ('decission', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='decission', to='game.Player')),
                ('player1', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player1', to='game.Player')),
                ('player2', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player2', to='game.Player')),
                ('player3', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player3', to='game.Player')),
                ('player4', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player4', to='game.Player')),
                ('small_blind', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='small_blind', to='game.Player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tablee', to='game.Table'),
        ),
    ]
