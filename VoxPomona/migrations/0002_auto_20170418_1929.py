# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VoxPomona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chid', models.IntegerField()),
                ('content', models.TextField()),
                ('decision', models.IntegerField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VoxPomona.User', to_field='email')),
            ],
        ),
        migrations.CreateModel(
            name='ChangeVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField()),
                ('chid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VoxPomona.Change')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VoxPomona.User', to_field='email')),
            ],
        ),
        migrations.CreateModel(
            name='Clause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('content', models.TextField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VoxPomona.User', to_field='email')),
            ],
        ),
        migrations.CreateModel(
            name='CommentVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VoxPomona.Comment')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VoxPomona.User', to_field='email')),
            ],
        ),
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petitionID', models.IntegerField()),
                ('category', models.CharField(max_length=2)),
                ('open_time', models.DateField()),
                ('close_time', models.DateField()),
                ('threshold', models.IntegerField()),
                ('finalized', models.BooleanField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VoxPomona.User', to_field='email')),
            ],
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('petitionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VoxPomona.Petition')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VoxPomona.User', to_field='email')),
            ],
        ),
        migrations.AddField(
            model_name='clause',
            name='petitionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VoxPomona.Petition'),
        ),
    ]