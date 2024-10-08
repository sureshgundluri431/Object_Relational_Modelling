# Generated by Django 5.1 on 2024-10-03 01:31

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('Game', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('name', models.ForeignKey(on_delete=app.models.Player, to='app.player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='Game',
            field=models.ForeignKey(on_delete=app.models.Team, to='app.team'),
        ),
    ]
