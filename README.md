<center><h1>stark组件</h1></center>

## 开始

介绍：
　　stark组件，是一个帮助开发者快速实现数据库表的增删改查+的组件。
目标：
　　10s 中完成一张表的增删改查。

- django项目启动时，自定义执行某个py文件。

  ```
  django启动时，且在读取项目中 路由加载 之前执行某个py文件。
  
  在任意app的apps.py中的Config类中定义ready方法，并调用autodiscover_modules
      from django.apps import AppConfig
      from django.utils.module_loading import autodiscover_modules
  
  
      class App01Config(AppConfig):
      name = 'app01'
  
      def ready(self):
          autodiscover_modules('xxxx')
  
  
  django在启动时，就会去已注册的所有app的目录下找 xxxx.py 并自动导入。
  
  
  如果执行两次，是因为django内部自动重启导致：
      python manage.py runserver 120.0.0.1:8001 --noreload
  
  提示：
      如果xxxx.py执行的代码向 “某个神奇的地方” 放入了一些值。之后的路由加载时，可以去“某个神奇的地方”读取到原来设置的值。
  ```

  

- 单例模式

  ```
  单，一个。
  例，实例、对象。
  
  通过利用Python模块导入的特性：在Python中，如果已经导入过的文件再次被重新导入时候，python不会再重新解释一遍，而是选择从内存中直接将原来导入的值拿来用。
  xxxx.py
      class AdminSite(object):
          pass
      site = AdminSite() # 为AdminSite类创建了一个对象（实例）
  app.py
      import utils
      print(utils.site)
  
      import utils
      print(utils.site)
  
  
  提示：
      如果以后存在一个单例模式的对象，可以先在此对象中放入一个值，然后再在其他的文件中导入该对象，通过对象再次讲值获取到。
  ```

  

- django路由分发的本质：include

  ```
  方式一：
      from django.conf.urls import url,include
  
      urlpatterns = [
          url(r'^web/', include("app01.urls")),
      ]
  
  方式二：
      include函数主要返回有三个元素的元组。
      from django.conf.urls import url,include
      from app01 import urls
      urlpatterns = [
          url(r'^web/', (urls, app_name, namespace)), # 第一个参数是urls文件对象，通过此对象可以获取urls.patterns获取分发的路由。
      ]
  
  
      在源码内部，读取路由时：
          如有第一个参数有：urls.patterns 属性，那么子路由就从该属性中后去。
          如果第一个参数无：urls.patterns 属性，那么子路由就是第一个参数。
  
  方式三：
      urlpatterns = [
          url(r'^web/', ([
              url(r'^index/', views.index),
              url(r'^home/', views.home),
          ], app_name, namespace)), # 第一个参数是urls文件对象，通过此对象可以获取urls.patterns获取分发的路由。
      ]
  ```

  

## 2. 组件开发

- 创建 django project
- 创建基础的业务表
   - app01
      - 部门表
      - 用户表
   - app02
      - 主机表

- 三张表增删改查
  - 分析

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

  - 创建

&emsp;为app中的每个model类自动创建URL和相关视图函数
