# Generated by Django 2.2.7 on 2019-11-15 21:55

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_course_is_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '轮播课程',
                'verbose_name_plural': '轮播课程',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('course.course',),
        ),
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='课程详情'),
        ),
    ]