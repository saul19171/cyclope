# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-28 18:29
from __future__ import unicode_literals

import autoslug.fields
import cyclope.core.user_profiles.models
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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=cyclope.core.user_profiles.models._slug_populate, unique=True)),
                ('avatar', models.ImageField(blank=True, upload_to=b'avatars/', verbose_name='avatar')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='city')),
                ('about', models.TextField(blank=True, max_length=1000, verbose_name='about myself')),
                ('public', models.BooleanField(default=True, help_text='Choose whether your profile info should be publicly visible or not', verbose_name='public')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
