from django.db import models


# Create your models here.


class Depart(models.Model):
    """
    部门表
    """
    title = models.CharField(verbose_name="部门名称", max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(verbose_name="姓名", max_length=32)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.IntegerField(verbose_name="性别", choices=gender_choices, default=1)

    class_choices = (
        (1, '大一'),
        (2, '大二'),
        (3, '大三'),
        (4, '大四'),
    )
    classes = models.IntegerField(verbose_name="年级", choices=class_choices, default=1)
    age = models.CharField(verbose_name="年龄", max_length=32)
    email = models.CharField(verbose_name="邮箱", max_length=32)
    depart = models.ForeignKey(verbose_name="部门", to="Depart", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
