# Generated by Django 2.2.7 on 2019-11-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_teacher_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorganization',
            name='tag',
            field=models.CharField(default='全国知名', max_length=10, verbose_name='机构标签'),
        ),
    ]