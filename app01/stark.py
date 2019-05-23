#!/usr/bin/python
# _*_ coding: utf-8 _*_
from django.conf.urls import url
from django.shortcuts import HttpResponse
from stark.service.v1 import site, StarkHandler
from app01 import models


class DepartHandler(StarkHandler):
    list_display = ["id", "title"]


class UserInfoHandler(StarkHandler):
    # 定制页面显示的列
    list_display = ["name", "age", "email"]

    def get_list_display(self):
        """
        :return:
        """
        return ["name"]


site.register(models.Depart, DepartHandler)
site.register(models.UserInfo, UserInfoHandler)
# site.register(models.UserInfo, prev="private")
# site.register(models.UserInfo, prev="public")
