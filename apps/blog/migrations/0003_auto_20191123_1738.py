# Generated by Django 2.2.7 on 2019-11-23 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191122_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Category', verbose_name='教程分类'),
        ),
    ]
