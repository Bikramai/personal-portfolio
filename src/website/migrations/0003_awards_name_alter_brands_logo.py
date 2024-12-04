# Generated by Django 5.0.7 on 2024-10-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_about_options_alter_awards_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='awards',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brands',
            name='logo',
            field=models.ImageField(help_text='Brands You have collaborated with 50x50 [png]', upload_to='brands'),
        ),
    ]
