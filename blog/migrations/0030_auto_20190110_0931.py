# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-10 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_remove_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(),
        ),
    ]