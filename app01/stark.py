#!/usr/bin/python
# _*_ coding: utf-8 _*_
from django.conf.urls import url
from django.shortcuts import HttpResponse
from django.urls import reverse
from stark.service.v1 import site, StarkHandler, get_choice_text
from app01 import models
from django.utils.safestring import mark_safe


class DepartHandler(StarkHandler):
    list_display = ["id", "title", StarkHandler.display_edit, StarkHandler.display_del]


class UserInfoHandler(StarkHandler):

    # def display_depart(self, obj=None, is_header=None):
    #     if is_header:
    #         return "部门"
    #     else:
    #         return obj.depart.title
    # 定制页面显示的列
    # list_display = ["name", "age", "email",display_depart, StarkHandler.display_edit, StarkHandler.display_del]

    def display_gender(self, obj=None, is_header=None):
        if is_header:
            return "性别"
        else:
            return obj.get_gender_display()

    list_display = ["name",
                    get_choice_text("性别", "gender"),
                    get_choice_text("年级", "classes"),
                    display_gender,
                    "age", "email", "depart", StarkHandler.display_edit, StarkHandler.display_del]
    # per_page_count = 20
    per_page_count = 1
    # def get_list_display(self):
    #     """
    #     自定义扩展,例如 根据用户的不同显示不同的列
    #     :return:
    #     """
    #     return ["name"]


site.register(models.Depart, DepartHandler)
site.register(models.UserInfo, UserInfoHandler)
# site.register(models.UserInfo, prev="private")
# site.register(models.UserInfo, prev="public")
