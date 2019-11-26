# Generated by Django 2.2.7 on 2019-11-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_tutorial_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='degree',
            field=models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], default='cj', max_length=2, verbose_name='课程难度'),
        ),
    ]
