# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 08:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('permabots', '0005_auto_20160428_0510'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='kikchatstate',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='kikmessage',
            unique_together=set([]),
        ),
    ]
