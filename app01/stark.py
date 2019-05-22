#!/usr/bin/python
# _*_ coding: utf-8 _*_
from django.shortcuts import HttpResponse
from stark.service.v1 import site
from app01 import models


class DepartHandler(object):

    def __init__(self, model_class):
        self.model_class = model_class

    def changelist_view(self, request):
        """
        列表页面
        :param request:
        :return:
        """
        return HttpResponse("部门列表页面")

    def add_view(self, request):
        """
        增加页面
        :param request:
        :return:
        """
        pass

    def change_view(self, request, pk):
        """
        编辑页面
        :param request:
        :return:
        """
        pass

    def delete_view(self, request, pk):
        """
        删除页面
        :param request:
        :return:
        """
        pass


class UserInfoHandler(object):

    def __init__(self, model_class):
        self.model_class = model_class

    def changelist_view(self, request):
        """
        列表页面
        :param request:
        :return:
        """
        return HttpResponse("用户列表页面")

    def add_view(self, request):
        """
        增加页面
        :param request:
        :return:
        """
        pass

    def change_view(self, request, pk):
        """
        编辑页面
        :param request:
        :return:
        """
        pass

    def delete_view(self, request, pk):
        """
        删除页面
        :param request:
        :return:
        """
        pass


site.register(models.Depart, DepartHandler)
site.register(models.UserInfo, UserInfoHandler)
