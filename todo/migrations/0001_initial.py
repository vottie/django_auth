# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('memo', models.CharField(max_length=128, verbose_name='Memo')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='todo')),
            ],
        ),
    ]
