# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 19:31
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import enumfields.fields
import model_utils.fields
import socialhome.enums


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_set_user_handle_not_null'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('nickname', models.CharField(help_text='Usually username, for local users at least.', max_length=64, unique=True, verbose_name='Nickname')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('guid', models.CharField(editable=False, max_length=255, unique=True, verbose_name='GUID')),
                ('handle', models.CharField(editable=False, max_length=255, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='Handle')),
                ('rsa_private_key', models.TextField(editable=False, null=True, verbose_name='RSA private key')),
                ('rsa_public_key', models.TextField(editable=False, null=True, verbose_name='RSA public key')),
                ('visibility', enumfields.fields.EnumIntegerField(default=3, enum=socialhome.enums.Visibility, verbose_name='Profile visibility')),
                ('image_url_large', models.URLField(blank=True, verbose_name='Image - large')),
                ('image_url_medium', models.URLField(blank=True, verbose_name='Image - medium')),
                ('image_url_small', models.URLField(blank=True, verbose_name='Image - small')),
                ('location', models.CharField(blank=True, max_length=128, verbose_name='Location')),
                ('nsfw', models.BooleanField(default=False, help_text='Should users content be considered NSFW?', verbose_name='NSFW')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='Created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='Modified')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
