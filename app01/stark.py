#!/usr/bin/python
# _*_ coding: utf-8 _*_
from django.conf.urls import url
from django.shortcuts import HttpResponse, redirect
from django.urls import reverse
from stark.service.v1 import site, StarkHandler, get_choice_text, StarkModelForm, Option
from app01 import models
from django import forms
from django.utils.safestring import mark_safe


class DepartHandler(StarkHandler):
    list_display = [StarkHandler.display_checkbox, "id", "title", StarkHandler.display_edit, StarkHandler.display_del]
    has_add_btn = True
    action_list = [StarkHandler.action_multi_delete, ]


class UserInfoModelForm(StarkModelForm):
    # xx = forms.CharField() # 新

    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        fields = ["name", "gender", "classes", "age", "email"]


class MyOption(Option):
    def get_db_condition(self, request, *args, **kwargs):
        return {'id__gt': request.GET.get("nid")}


class UserInfoHandler(StarkHandler):

    def display_gender(self, obj=None, is_header=None):
        if is_header:
            return "性别"
        else:
            return obj.get_gender_display()

    list_display = [
        StarkHandler.display_checkbox,
        "name",
        get_choice_text("性别", "gender"),
        get_choice_text("年级", "classes"),
        display_gender,
        "age", "email", "depart", StarkHandler.display_edit, StarkHandler.display_del]
    # per_page_count = 20
    per_page_count = 10
    # has_add_btn = False
    # model_form_class = UserInfoModelForm
    order_list = ['id']  # 排序，sql中的order

    # 姓名中含有关键字或者邮箱中含有关键字
    search_list = ["name__contains", "email__contains"]  # 模糊匹配

    # search_list = ["name", "email"] # 精确匹配
    # search_list = ["name__contains"]

    action_list = [StarkHandler.action_multi_delete, ]

    # def multi_init(self, request, *args, **kwargs):
    # multi_init.text = "批量处理"
    # action_list = [multi_delete, multi_init]
    # def save(self, form, is_update=False):
    #     form.instance.depart_id = 1
    #     form.save()

    search_group = [
        Option("gender"),
        Option("depart", db_condition={'id__gt': 2}),
        # Option("depart", {'id__gt': 1}),
        # Option("gender", text_func=lambda field_object: field_object[1]+'666'),
    ]


class DeployHandler(StarkHandler):
    # 自定制显示数据
    # list_display = ['title','status']
    list_display = ['title', get_choice_text("状态", "status"), StarkHandler.display_edit, StarkHandler.display_del]
    per_page_count = 20
    # per_page_count = 1   # 每页显示多少数据
    # has_add_btn = False  # 是否有添加按钮

    # def save(self, form, is_update=False):
    #     form.instance.depart_id = 1
    #     form.save()
    search_list = ["title__contains"]


site.register(models.Depart, DepartHandler)
site.register(models.UserInfo, UserInfoHandler)
site.register(models.Deploy, DeployHandler)
# site.register(models.UserInfo, prev="private")
# site.register(models.UserInfo, prev="public")
