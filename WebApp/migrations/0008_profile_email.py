# Generated by Django 3.2.8 on 2021-11-10 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0007_auto_20211109_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
