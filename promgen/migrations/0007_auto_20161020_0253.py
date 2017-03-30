# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 02:53


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promgen', '0006_auto_20161019_1214'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='exporter',
            unique_together=set([('job', 'port', 'project')]),
        ),
        migrations.AlterUniqueTogether(
            name='host',
            unique_together=set([('name', 'farm')]),
        ),
    ]