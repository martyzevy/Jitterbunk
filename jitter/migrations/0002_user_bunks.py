# Generated by Django 3.2.16 on 2024-06-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bunks',
            field=models.ManyToManyField(to='jitter.Bunk'),
        ),
    ]
