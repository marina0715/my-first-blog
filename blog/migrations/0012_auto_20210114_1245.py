# Generated by Django 2.2.16 on 2021-01-14 03:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.TextField(validators=[django.core.validators.URLValidator()]),
        ),
    ]