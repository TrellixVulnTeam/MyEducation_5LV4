# Generated by Django 2.2.7 on 2019-11-24 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191124_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ManyToManyField(to='blog.Section', verbose_name='章节外键-多对多'),
        ),
    ]
