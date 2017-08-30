# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 05:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('radarbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='radar.RadarBaseModel')),
                ('name', models.CharField(max_length=255)),
                ('website', models.URLField(blank=True, default=None, null=True)),
                ('linkedin', models.URLField(blank=True, default=None, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
            bases=('radar.radarbasemodel',),
        ),
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('radarbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='radar.RadarBaseModel')),
                ('name', models.CharField(max_length=255)),
                ('linkedin', models.URLField(blank=True, default=None, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('works_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works_at', to='radar.Company')),
            ],
            bases=('radar.radarbasemodel',),
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='opportunity',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radar.Industry'),
        ),
    ]
