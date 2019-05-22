#!/usr/bin/python
# _*_ coding: utf-8 _*_
from django.shortcuts import HttpResponse
from stark.service.v1 import site, StarkHandler
from app02 import models


class HostHandler(StarkHandler):

    pass


class RoleHandler(StarkHandler):

    pass


class ProjectHandler(StarkHandler):

    pass


site.register(models.Host, HostHandler)
site.register(models.Role, RoleHandler)
site.register(models.Project, ProjectHandler)


