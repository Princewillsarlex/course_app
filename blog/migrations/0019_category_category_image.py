# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-07 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_course_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default=1, upload_to='category-image/'),
            preserve_default=False,
        ),
    ]