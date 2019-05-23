"""luffy_stark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from stark.service.v1 import site


# print(site._registry)
"""
[{'model_class': <class 'app01.models.Depart'>, 'handler_class': <app01.stark.DepartHandler object at 0x000001D91946D940>},
 {'model_class': <class 'app01.models.UserInfo'>, 'handler_class': <app01.stark.UserInfoHandler object at 0x000001D91946DA20>}, 
 {'model_class': <class 'app02.models.Host'>, 'handler_class': <app02.stark.HostHandler object at 0x000001D91946DE80>}]
"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stark/', site.urls),
]
