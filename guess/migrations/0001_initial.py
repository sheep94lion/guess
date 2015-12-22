# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuessSubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=400)),
                ('choiceA', models.CharField(max_length=100)),
                ('choiceB', models.CharField(max_length=100)),
                ('stepsA', models.IntegerField()),
                ('stepsB', models.IntegerField()),
            ],
        ),
    ]
