# Generated by Django 2.2.1 on 2019-06-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_deploy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deploy',
            name='status',
            field=models.IntegerField(choices=[(1, '在线'), (2, '离线'), (3, '未知')], verbose_name='状态'),
        ),
    ]
