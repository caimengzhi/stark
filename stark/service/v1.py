#!/usr/bin/python
# _*_ coding: utf-8 _*_
from django.conf.urls import url
from django.shortcuts import HttpResponse


class StarkSite(object):
    def __init__(self):
        self._registry = []
        self.app_name = "stark"
        self.namespace = "stark"

    def register(self, model_class, handler_class):
        """
        :param model_class: 是models中数据相关类
        :param handler_class: 处理请求的视图函数所在的类
        :return:
        """
        """
        self._registry = [
            {"model_class":model_class.Depart, "handler":DepartHandler(models.Depart)},
            {"model_class":model_class.UserInfo, "handler":UseInfoHandler(models.UserInfo)},
            {"model_class":model_class.Host, "handler":HostHandler(models.Host)},
        ]
        """
        self._registry.append({"model_class": model_class, "handler": handler_class(model_class)})

    def get_urls(self):
        patterns = []
        for item in self._registry:
            model_class = item["model_class"]
            handler = item["handler"]
            app_label, model_name = model_class._meta.app_label, model_class._meta.model_name
            patterns.append(url(r'%s/%s/list/$'%(app_label, model_name,), handler.changelist_view))
            patterns.append(url(r'%s/%s/add/$'%(app_label, model_name,), handler.add_view))
            patterns.append(url(r'%s/%s/change/(\d+)/$'%(app_label, model_name,), handler.change_view))
            patterns.append(url(r'%s/%s/del/(\d+)/$'%(app_label, model_name,), handler.delete_view))

            # print("app-name = ", model_class._meta.app_label)  # 获取app name
            # print("table-name = ", model_class._meta.model_name)  # 获取 类的表名称
            # app01.models.Depart'
            #   /app01/depart/list/
            #   /app01/depart/add/
            #   /app01/depart/edit(\d+)/
            #   /app01/depart/del(\d+)/

            # patterns.append(url(r'x1/', lambda request: HttpResponse('x1')),)
            # patterns.append(url(r'x2/', lambda request: HttpResponse('x2')),)
        return patterns

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.namespace


site = StarkSite()
