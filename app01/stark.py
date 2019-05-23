#!/usr/bin/python
# _*_ coding: utf-8 _*_
from django.conf.urls import url
from django.shortcuts import HttpResponse
from stark.service.v1 import site, StarkHandler
from app01 import models
from django.utils.safestring import mark_safe


class DepartHandler(StarkHandler):
    list_display = ["id", "title"]


class UserInfoHandler(StarkHandler):

    def display_edit(self, obj=None, is_header=None):
        """
        自定义页面显示的列，包括表头和内容
        :param obj:
        :param is_header:
        :return:
        """
        if is_header:
            return "编辑"
        return mark_safe("<a href='http://www.jd.com'>编辑</a>")

    def display_del(self, obj=None, is_header=None):
        if is_header:
            return "删除"
        return mark_safe("<a href='http://www.jd.com'>删除</a>")
    # 定制页面显示的列
    list_display = ["name", "age", "email", display_edit, display_del]

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
