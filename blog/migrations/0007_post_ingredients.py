# Generated by Django 2.2.16 on 2020-12-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_motion'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ingredients',
            field=models.CharField(default='', max_length=2, verbose_name='食材数'),
        ),
    ]
