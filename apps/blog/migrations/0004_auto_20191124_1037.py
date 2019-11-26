# Generated by Django 2.2.7 on 2019-11-24 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191123_1738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': '章节', 'verbose_name_plural': '章节'},
        ),
        migrations.AlterModelOptions(
            name='tutorial',
            options={'verbose_name': '教程', 'verbose_name_plural': '教程'},
        ),
        migrations.RemoveField(
            model_name='section',
            name='chapbook',
        ),
        migrations.AddField(
            model_name='section',
            name='tutorial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Tutorial', verbose_name='Tutorial外鍵'),
        ),
    ]
