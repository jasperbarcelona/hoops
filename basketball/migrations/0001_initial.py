# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-29 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('street', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('region', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=60)),
                ('image', models.TextField()),
                ('added_by_user_id', models.IntegerField(default=None)),
                ('added_by_user_name', models.CharField(default=None, max_length=60)),
                ('verified_by_admin_id', models.IntegerField()),
                ('verified_by_admin_name', models.CharField(max_length=60)),
                ('verified', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('open', 'open'), ('closed', 'closed'), ('ongoing', 'ongoing'), ('finished', 'finished')], max_length=255)),
                ('court_id', models.IntegerField()),
                ('court_name', models.CharField(max_length=60)),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('created_by_user_id', models.IntegerField()),
                ('created_by_user_name', models.CharField(max_length=60)),
                ('game_type', models.CharField(choices=[('private', 'Invite only'), ('public', 'Open for everyone')], max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('city', models.CharField(max_length=60)),
                ('region', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('msisdn', models.CharField(max_length=16)),
                ('city', models.CharField(max_length=60)),
                ('region', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=60)),
                ('height', models.FloatField()),
                ('average_rating', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('game_id', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'pending'), ('going', 'going'), ('declined', 'declined')], max_length=60)),
                ('invited_by_user_id', models.IntegerField(default=None)),
                ('invited_by_user_name', models.CharField(default=None, max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('team_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('team_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
