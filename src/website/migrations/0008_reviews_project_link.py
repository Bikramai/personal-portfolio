# Generated by Django 5.0.7 on 2024-10-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_workexperience_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='project_link',
            field=models.URLField(default=1, help_text='Link to the project'),
            preserve_default=False,
        ),
    ]
