# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='memo',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='scene1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='scene2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='station',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='visited_times',
            field=models.IntegerField(null=True),
        ),
    ]