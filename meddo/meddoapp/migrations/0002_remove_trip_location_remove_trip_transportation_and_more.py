# Generated by Django 5.0 on 2024-04-30 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meddoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='location',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='transportation',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='user',
        ),
    ]