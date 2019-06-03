#!/usr/bin/python
# _*_ coding: utf-8 _*_
from django.conf.urls import url
from django.shortcuts import HttpResponse
from django.urls import reverse
from stark.service.v1 import site, StarkHandler, get_choice_text, StarkModelForm
from app01 import models
from django import forms
from django.utils.safestring import mark_safe


class DepartHandler(StarkHandler):
    list_display = ["id", "title", StarkHandler.display_edit, StarkHandler.display_del]
    has_add_btn = True


class UserInfoModelForm(StarkModelForm):
    # xx = forms.CharField() # 新

    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        fields = ["name", "gender", "classes", "age", "email"]


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
    model_form_class = UserInfoModelForm

    def save(self, form, is_update=False):
        form.instance.depart_id = 1
        form.save()


class DeployHandler(StarkHandler):
    # 自定制显示数据
    # list_display = ['title','status']
    list_display = ['title', get_choice_text("状态", "status"), StarkHandler.display_edit, StarkHandler.display_del]
    # per_page_count = 20
    # per_page_count = 1   # 每页显示多少数据
    # has_add_btn = False  # 是否有添加按钮

    # def save(self, form, is_update=False):
    #     form.instance.depart_id = 1
    #     form.save()


site.register(models.Depart, DepartHandler)
site.register(models.UserInfo, UserInfoHandler)
site.register(models.Deploy, DeployHandler)
# site.register(models.UserInfo, prev="private")
# site.register(models.UserInfo, prev="public")
