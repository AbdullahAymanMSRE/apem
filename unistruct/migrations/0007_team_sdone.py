# Generated by Django 3.0.5 on 2020-04-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unistruct', '0006_team_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='sdone',
            field=models.BooleanField(default=False),
        ),
    ]
