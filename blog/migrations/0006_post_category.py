# Generated by Django 2.2.16 on 2021-01-13 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.Category', verbose_name='カテゴリー'),
            preserve_default=False,
        ),
    ]
