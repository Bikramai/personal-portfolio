# Generated by Django 5.0.7 on 2024-10-28 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_awards_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awards',
            name='awarding_organization',
        ),
    ]
