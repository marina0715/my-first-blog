# Generated by Django 2.2.16 on 2021-01-13 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210114_0657'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'レシピ', 'verbose_name_plural': 'レシピ'},
        ),
    ]
