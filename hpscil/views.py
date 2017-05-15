# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from hpscil.models import *
from filterHtml import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger,InvalidPage

# Create your views here.
#主页
def index(request):
    people_list=people.objects.all()[:4]
    teamInfo_list=teamInfo.objects.all()[:4]
    research_list=research.objects.all().order_by("-time")[:4]
    carousel_list=news.objects.order_by("-time")[:5]
    return render(request,'index.html',locals())
    
#研究成果页面
def allresearch(request):
    research_list=research.objects.all().order_by("-time")
    teamInfo_list=teamInfo.objects.all()
    return render(request,'research.html',locals())
#研究成果详细信息
def researchinfo(request):
    if request.method=='GET':
        uid=request.GET.get('id')
        try:
            r=research.objects.get(id=uid)
        except :
            pass
    return render(request,'research_detail.html',locals())

#实验室信息页面
def libinfo(request):
    teamInfo_list=teamInfo.objects.all()
    return render(request,'libinfo.html',locals())

#实验室新闻页面
def libnews(request):
    teamInfo_list=teamInfo.objects.all()
    news_list=news.objects.order_by("-time")
    paginator=Paginator(news_list,10)#分页，每个页面10条记录
    try:
        page=int(request.GET.get('page',1))
        news_list=paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        news_list=paginator.page(1)
    return render(request,'news.html',locals())

#团队成员页面
def teammembers(request):
    leadship_list=people.objects.filter(isleadship=1)
    Postdoctoral_list=people.objects.filter(degree=0,title=4)
    Doctor_list=people.objects.filter(degree=1,title=4)
    Master_list=people.objects.filter(degree=2,title=4)
    Undergraduate_list=people.objects.filter(degree=3,title=4)
    Graduate_list=people.objects.filter(degree=4,title=4)
    teamInfo_list=teamInfo.objects.all()
    return render(request,'teammembers.html',locals())

#团队信息详情页
def memberinfo(request):
    if request.method=='GET':
        uid=request.GET.get('id')
        try:
            p=people.objects.get(id=uid)
        except :
            pass
    return render(request,'memberinfo.html',locals())

#关于页面
def about(request):
    teamInfo_list=teamInfo.objects.all()
    return render(request,'about.html',locals())

#新闻详情页
def detail(request):
    teamInfo_list=teamInfo.objects.all()
    uid=request.GET.get('id')
    article=news.objects.get(id=uid)
    return render(request,'article_detail.html',locals())

#实验室活动
def activitys(request):
    teamInfo_list=teamInfo.objects.all()
    activity_list=activity.objects.all()
    return render(request,"activity.html",locals())

#实验室活动详情页
def activitysinfo(request):
    teamInfo_list=teamInfo.objects.all()
    uid=request.GET.get('id')
    act=activity.objects.get(id=uid)
    return render(request,'activity_detail.html',locals())

#行业动态    
def trends(request):
    teamInfo_list=teamInfo.objects.all()
    trends_list=tb_trends.objects.all().order_by('-time')
    return render(request,'trends.html',locals())

