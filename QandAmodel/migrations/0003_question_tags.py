# Generated by Django 3.2.4 on 2021-07-03 19:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QandAmodel', '0002_auto_20210701_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), blank=True, default=list, size=None),
        ),
    ]
