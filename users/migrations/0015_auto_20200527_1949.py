# Generated by Django 3.0.5 on 2020-05-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20200515_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='doctor',
            field=models.BooleanField(default=True, verbose_name='professor'),
        ),
    ]
