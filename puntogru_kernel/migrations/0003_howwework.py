# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-08 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puntogru_kernel', '0002_auto_20170608_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowWeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('img', models.ImageField(upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u044d\u0442\u0430\u043f',
                'verbose_name_plural': '\u042d\u0442\u0430\u043f\u044b \u0440\u0430\u0431\u043e\u0442',
            },
        ),
    ]