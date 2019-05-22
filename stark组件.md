```
第二部: stark 组件
    介绍:
        stark 组件，是一个帮助开发者快速实现数据库表的增删改查

    目标:
        10s 完成一张表增删改查

    前戏:
        1. django项目启动时候，自动执行某个py文件
            django启动时候，路由加载之前，执行某个py文件
            在任意app的apps.py中config类中定义ready方法。并调用autodiscover_modules
            from django.apps import AppConfig
            from django.utils.module_loading import autodiscover_modules

            class App01Config(AppConfig):
                name = 'app01'

                def ready(self):
                    autodiscover_modules('文件名xxx')

            django在启动时候，就会去已注册的所有app的目录下找xxx.py 并导入
                如果执行两次，是因为django内部自动重启导致，不自动重启的话如下
                python manage.py runserver 127.0.0.1:8000 --noreload

            提示: 如果xxx.py 执行的代码，向"某个神奇的地方"，放入了一些值,之后的路由加载时候，可以去"某个神奇的地方"读取到原来设置的值。

        2. 单例模式
            实例化一个对象。

            提示:
                如果以后存在一个单例模式的对象，可以先在此对象中放入一个值，然后子啊其他的文件中导入该对象，通过对象再次将值获取到。

        3. django 路由分发的本质 include
        方式1:
            from django.conf.urls import url, include
            urlpatterns = [
                url(r'^web/', include("app01.urls")),
            ]
            include 函数主要返回三个元素的元祖
        方式2:
            from django.conf.urls import url, include
            from app01 import urls
            urlpatterns = [
                url(r'^web/', (urls,app_name,namespace), # 第一个参数是urls文件对象，通过此对象可以获取urls,patterns获取分发的路由
            ]

            在源码内部，读取路由时，
                第一个参数有: urls.patterns属性，那么子路由就从该属性中去获取
                第一个参数无: urls.patterns属性，那么子路由就是第一个参数

        方式3:
            from django.conf.urls import url, include
            from app01 import urls
            urlpatterns = [
                url(r'^web/', ([
                    url(r'^index/', views.index),
                    url(r'^home/', views.home),
                ],app_name,namespace), # 第一个参数是urls文件对象，通过此对象可以获取urls,patterns获取分发的路由
            ]
```

## 开始

### 1. 创建 django project



### 2. 创建基础的业务表

 - app01
    - 部门表
    - 用户表
 - app02
    - 主机表

### 3. 三张表增删改查

#### 3.1 分析

- 为每张表创建4个url

- 为每张表创建4个视图函数

  app01/models.py

  - Depart
    - /app01/depart/list/
    - /app01/depart/add/
    - /app01/depart/edit(\d+)/
    - /app01/depart/del(\d+)/
  - UserInfo
    - /app01/userinfo/list/
    - /app01/userinfo/add/
    - /app01/userinfo/edit(\d+)/
    - /app01/userinfo/del(\d+)/

  app02

  - Host
    - /app02/host/list/
    - /app02/host/add/
    - /app02/host/edit(\d+)/
    - /app02/host/del(\d+)/

#### 3.2 创建

&emsp;为app中的每个model类自动创建URL和相关视图函数

https://www.luffycity.com/micro/play/5660/1231