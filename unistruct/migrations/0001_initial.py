# Generated by Django 3.0.5 on 2020-04-19 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='unistruct.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='unistruct.Faculty')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='unistruct.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='unistruct.Faculty')),
            ],
        ),
    ]
