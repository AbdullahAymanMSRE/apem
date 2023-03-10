# Generated by Django 3.0.5 on 2020-05-05 22:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researches', '0007_auto_20200504_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentresearch',
            name='passed',
        ),
        migrations.AddField(
            model_name='studentresearch',
            name='axes',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='studentresearch',
            name='conclusions',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='studentresearch',
            name='content',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='studentresearch',
            name='intro',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='studentresearch',
            name='references',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
