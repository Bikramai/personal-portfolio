# Generated by Django 5.0.7 on 2024-10-28 22:03

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_contactme'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='client_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='over_view',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='service_provided',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=tinymce.models.HTMLField(help_text='Description of the project'),
        ),
    ]