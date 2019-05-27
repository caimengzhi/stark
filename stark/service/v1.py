#!/usr/bin/python
# _*_ coding: utf-8 _*_
from django.conf.urls import url
from django.shortcuts import HttpResponse, render
from types import FunctionType
from django.urls import reverse
from django.utils.safestring import mark_safe


def get_choice_text(title, filed):
    """
    对于stark组件中定义列时，choice如果想要显示中文信息，调用此方法即可
    :param title: 期望页面显示的表头
    :param filed: 字段名称
    :return:
    """

    def inner(self, obj=None, is_header=None):
        if is_header:
            return title
        method = "get_%s_display" % filed
        return getattr(obj, method)()

    return inner


class StarkHandler(object):
    list_display = []
    def display_edit(self, obj=None, is_header=None):
        if is_header:
            return "编辑"
        name = "%s:%s" % (self.site.namespace, self.get_change_url_name)
        url = reverse(name, args=(obj.pk,))
        return mark_safe("<a href='%s'>编辑</a>" %url)

    def display_del(self, obj=None, is_header=None):
        if is_header:
            return "删除"
        name = "%s:%s" % (self.site.namespace, self.get_delete_url_name)
        url = reverse(name, args=(obj.pk,))
        return mark_safe("<a href='%s'>删除</a>" % url)

    def get_list_display(self):
        """
        显示自定义扩展:  例如根据用户的不同，显示不同的列，预留的自定义扩展
        获取页面上应该显示的列
        :return:
        """
        value = []
        value.extend(self.list_display)
        return value

    def __init__(self, site, model_class, prev):
        self.site = site
        self.model_class = model_class
        self.prev = prev

    def changelist_view(self, request):
        """
        列表页面
        :param request:
        :return:
        """
        """
        # 访问 http://127.0.0.1:8000/stark/app01/depart/list/   --> self.model_class = app01.models.Depart
        # 访问 http://127.0.0.1:8000/stark/app01/userinfo/list/   --> self.model_class = app01.models.UserInfo
        # 访问 http://127.0.0.1:8000/stark/app02/role/list/   --> self.model_class = app02.models.Role
        # 访问 http://127.0.0.1:8000/stark/app02/host/list/   --> self.model_class = app02.models.Host
        #                                                site.register(models.Host, HostHandler)
        """
        # print(self.model_class)

        # 1. 处理表头
        # 访问: http://127.0.0.1:8000/stark/app01/userinfo/list/
        # 新页面要显示的列  ['name','age','email']
        # 用户访问的表  models.UserInfo
        list_display = self.get_list_display()
        header_list = []
        if list_display:
            for key_or_func in list_display:
                if isinstance(key_or_func,FunctionType): # 函数
                    verbose_name = key_or_func(self, obj=None, is_header=True)
                else:
                    verbose_name = self.model_class._meta.get_field(key_or_func).verbose_name
                header_list.append(verbose_name)
        else:
            header_list.append(self.model_class._meta.model_name)
        # 2. 处理表的内容 ["name","age"]
        """
        [
        obj,
        obj,
        obj
        ]
        """
        data_list = self.model_class.objects.all()
        """
        body_list = [
            ["蔡猛芝",30,610658552@qq.com],
            ["朱佳曦",3,zhujiaxi@cmz.com],
        ]
        """
        body_list = []
        for row in data_list: # 取出obj
            tr_list = []
            if list_display:
                for key_or_func in list_display:
                    if isinstance(key_or_func, FunctionType):  # 函数
                        tr_list.append(key_or_func(self,row,is_header=False))
                    else:
                        tr_list.append(getattr(row,key_or_func))
            else:
                tr_list.append(row)  # 没有定制显示，直接显示对象
            body_list.append(tr_list)
        # print("body_list = ",body_list)
        return render(
            request,
            "stark/changelist.html",
            {
                "data_list": data_list,
                "header_list": header_list,
                "body_list": body_list,
            }
        )

    def add_view(self, request):
        """
        增加页面
        :param request:
        :return:
        """
        return HttpResponse("添加页面")

    def change_view(self, request, pk):
        """
        编辑页面
        :param request:
        :return:
        """
        return HttpResponse("修改页面")

    def delete_view(self, request, pk):
        """
        删除页面
        :param request:
        :return:
        """
        return HttpResponse("删除页面")

    def get_url_name(self,param):
        app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name
        if self.prev:
            return "%s_%s_%s_%s" % (app_label, model_name,self.prev,param)
        return "%s_%s_%s" % (app_label, model_name,param,)

    @property
    def get_list_url_name(self):
        """
        获取列表页面URL的name
        :return:
        """
        return self.get_url_name("list")

    @property
    def get_add_url_name(self):
        """
        获取添加页面URL的name
        :return:
        """
        return self.get_url_name("add")

    @property
    def get_change_url_name(self):
        """
        获取修改页面URL的name
        :return:
        """
        return self.get_url_name("change")

    @property
    def get_delete_url_name(self):
        """
        获取删除页面的URL的name
        :return:
        """
        return self.get_url_name("delete")

    def get_urls(self):
        app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name

        patterns = [
            url(r'^list/$', self.changelist_view, name=self.get_list_url_name),
            url(r'^add/$', self.add_view, name=self.get_add_url_name),
            url(r'^change/(\d+)/$', self.change_view, name=self.get_change_url_name),
            url(r'^delete/(\d+)/$', self.delete_view, name=self.get_delete_url_name),
        ]
        patterns.extend(self.extra_urls())
        return patterns

    def extra_urls(self):
        return []


class StarkSite(object):
    def __init__(self):
        self._registry = []
        self.app_name = "stark"
        self.namespace = "stark"

    def register(self, model_class, handler_class=None, prev=None):
        """
        :param model_class: 是models中数据相关类
        :param handler_class: 处理请求的视图函数所在的类
        :param prev: 生成URL前缀
        :return:
        """
        """
        self._registry = [
            {"prev:":prev,"model_class":model_class.Depart, "handler":DepartHandler(models.Depart,prev)},
            {"prev:":private,"model_class":model_class.UserInfo, "handler":UseInfoHandler(models.UserInfo,prev)},
            {"prev:":prev,"model_class":model_class.Host, "handler":HostHandler(models.Host,prev)},
        ]
        """
        if not handler_class:
            handler_class = StarkHandler
        self._registry.append({"model_class": model_class, "handler": handler_class(self, model_class, prev), "prev": prev})

    def get_urls(self):
        patterns = []
        for item in self._registry:
            model_class = item["model_class"]
            handler = item["handler"]
            prev = item["prev"]
            app_label, model_name = model_class._meta.app_label, model_class._meta.model_name
            if prev:
                patterns.append(url(r'%s/%s/%s/' % (app_label, model_name, prev,), (handler.get_urls(), None, None)))
            else:
                patterns.append(url(r'%s/%s/' % (app_label, model_name,), (handler.get_urls(), None, None)))
        # print("patterns = ", patterns)
        return patterns

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.namespace


site = StarkSite()
