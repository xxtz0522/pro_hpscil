#encode=utf-8

"""Pro_hpscil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from hpscil.views import *

from . import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$',index),
    url(r'^research/',allresearch),
    url(r'^researchinfo/',researchinfo),
    url(r'^libinfo/',libinfo),
    url(r'^news/',libnews),
    url(r'^activity/',activitys),
    url(r'^activityinfo/',activitysinfo),
    url(r'^teammembers/',teammembers),
    url(r'^memberinfo/',memberinfo),
    url(r'^about/',about),
    url(r'^trends/',trends),
    url(r'^detail/',detail),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
admin.site.site_header = "HPSCIL Admin"
