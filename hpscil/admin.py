# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from hpscil.models import *
# Register your models here.

class people_admin(admin.ModelAdmin):   
    list_display=('name','age','sex','img','title','email','major','degree',)
    fileds=('name','age','sex','img','info','title','email','major','degree','isleadship',)
    search_fields=('name',)

class news_admin(admin.ModelAdmin):
    list_display=('title','time','author')
    fileds=('title','time','author','img','content')
    search_fields=('title',)

class teamInfo_admin(admin.ModelAdmin):
    list_display=('name','address','postcode','tel','email',)
    fileds=('name','address','postcode','tel','email',)
 
class research_admin(admin.ModelAdmin):
    list_display=('title','time','author')
    fileds=('title','time','author','img','content')
    search_fields=('title','author')

    
class activity_admin(admin.ModelAdmin):
    list_display=('topic','time','place','people_num',)
    fileds=('topic','time','place','people_num','thumbnail','content',)

class trends_admin(admin.ModelAdmin):
    list_display=('title','url','time',)
    fileds=('title','url','time',)

admin.site.register(people,people_admin)
admin.site.register(news,news_admin)
admin.site.register(research,research_admin)
admin.site.register(teamInfo,teamInfo_admin)
admin.site.register(activity,activity_admin)
admin.site.register(tb_trends,trends_admin)