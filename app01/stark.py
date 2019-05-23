#!/usr/bin/python
# _*_ coding: utf-8 _*_
from django.conf.urls import url
from django.shortcuts import HttpResponse
from stark.service.v1 import site, StarkHandler
from app01 import models


class DepartHandler(StarkHandler):

    def extra_urls(self):
        """
        额外的增加URL
        :return:
        """
        return [
            url(r'^detail/(\d+)/$', self.detail_view),
        ]

    def detail_view(self, request, pk):
        return HttpResponse("详细页面")


class UserInfoHandler(StarkHandler):
    def get_urls(self):
        """
        修改URL
        :return:
        """
        patterns = [
            url(r'^list/$', self.changelist_view),
            url(r'^add/$', self.add_view),
        ]
        return patterns


site.register(models.Depart, DepartHandler)
site.register(models.UserInfo, UserInfoHandler)
# site.register(models.UserInfo, prev="private")
# site.register(models.UserInfo, prev="public")
