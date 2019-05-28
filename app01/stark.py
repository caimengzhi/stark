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
    has_add_btn = True


class UserInfoHandler(StarkHandler):

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
    # has_add_btn = False


site.register(models.Depart, DepartHandler)
site.register(models.UserInfo, UserInfoHandler)
# site.register(models.UserInfo, prev="private")
# site.register(models.UserInfo, prev="public")
