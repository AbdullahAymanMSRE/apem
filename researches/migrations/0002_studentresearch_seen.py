# Generated by Django 3.0.5 on 2020-04-20 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresearch',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]
