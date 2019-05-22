#!/usr/bin/python
# _*_ coding: utf-8 _*_
from django.shortcuts import HttpResponse
from stark.service.v1 import site, StarkHandler
from app01 import models


class DepartHandler(StarkHandler):

    pass


class UserInfoHandler(StarkHandler):

    pass


site.register(models.Depart, DepartHandler)
site.register(models.UserInfo, UserInfoHandler)
