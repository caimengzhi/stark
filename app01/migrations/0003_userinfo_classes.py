# Generated by Django 2.2.1 on 2019-05-26 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190526_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='classes',
            field=models.IntegerField(choices=[(1, '大一'), (2, '大二'), (3, '大三'), (4, '大四')], default=1, verbose_name='年级'),
        ),
    ]
