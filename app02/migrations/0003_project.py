# Generated by Django 2.2.1 on 2019-05-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0002_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='项目名称')),
            ],
        ),
    ]
