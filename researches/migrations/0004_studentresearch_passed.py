# Generated by Django 3.0.5 on 2020-04-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researches', '0003_studentresearch_corrected'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresearch',
            name='passed',
            field=models.BooleanField(default=False),
        ),
    ]
