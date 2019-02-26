# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-26 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-modify_date',), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, verbose_name='CONTENT'),
        ),
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateField(auto_now=True, verbose_name='Create_date'),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, help_text='simple text', max_length=100, verbose_name='DESCRIPTION'),
        ),
        migrations.AddField(
            model_name='post',
            name='modify_date',
            field=models.DateField(auto_now=True, verbose_name='Modify_date'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='one word for title alias.', null=True, unique=True, verbose_name='SLUG'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='TITLE'),
        ),
        migrations.AlterModelTable(
            name='post',
            table='my_post',
        ),
    ]