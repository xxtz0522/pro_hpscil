# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django.utils.timezone as timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


#团队成员信息表
class people(models.Model):
    TITLE_CHOICES=(
        (0,'讲师'),
        (1,'副教授'),
        (2,'教授'),
        (3,'院士'),
        (4,'无'),
        )
    SEX_CHOICES=(
        (0,'男'),
        (1,'女'),
    )
    DEGREE_CHOICES=(
        (0,'博士后'),
        (1,'博士'),
        (2,'硕士'),
        (3,'本科'),
        (4,'往届毕业生'),
    )
    LEADSHIP_CHOICES=(
        (0,'否'),
        (1,'是'),
    )
    name=models.CharField('名字',max_length=50)#名字
    age=models.IntegerField('年龄',default=0)#年龄
    sex=models.IntegerField('性别',default=0,choices=SEX_CHOICES)#性别
    img=models.ImageField('头像')#头像
    info=RichTextUploadingField('简介',default='主人很懒，什么也没有留下!')#简介
    title=models.IntegerField('职称',default=0,choices=TITLE_CHOICES)#职称
    email=models.EmailField('邮箱')#邮箱
    major=models.CharField('研究方向',max_length=250)#研究方向
    degree=models.IntegerField('学位',default=2,choices=DEGREE_CHOICES)
    isleadship=models.IntegerField('领导小组',default=0,choices=LEADSHIP_CHOICES)
    def __unicode__(self, ):
        return self.name
    
#实验室新闻表
class news(models.Model):
    title=models.CharField('标题',max_length=120,)
    content=RichTextUploadingField('内容',)
    time=models.DateField('发布时间',default=timezone.now)
    author=models.CharField('编辑人',max_length=30)
    img=models.ImageField('轮播图(高度:400px)')
    
    def __unicode(self, ):
        return self.title
    
#研究成果信息表
class research(models.Model):
    title = models.CharField('标题',max_length=120,)
    content = RichTextUploadingField('内容',)
    time = models.DateField('发布时间', default = timezone.now)
    author = models.CharField('编辑人',max_length=30)
    img = models.ImageField('缩略图')
    
    def __unicode(self, ):
        return self.title

#团队信息表
class teamInfo(models.Model):
    name=models.CharField('团队名称',max_length=50,default='HPSCIL')
    address=models.CharField('实验室地址',max_length=250,default='湖北省武汉市洪山区鲁磨路388号\
中国地质大学（武汉）')
    postcode = models.CharField('邮编',max_length=10,default='430074')
    email = models.EmailField('邮箱')
    tel = models.CharField('联系方式',max_length=11,default='')
    info=RichTextUploadingField('详细介绍', default='')

    def __unicode__(self):
        return self.name        

class hitCount(models.Model):
    article=models.ForeignKey(news)
    amount=models.IntegerField(default=0)
    def __unicode__(self, ):
        return str(self.amount)
    
class activity(models.Model):
    thumbnail=models.ImageField('活动缩略图')
    topic=models.CharField('活动主题',max_length=100)
    time=models.DateTimeField('时间',default=timezone.now)
    place=models.CharField('地点',max_length=150)
    people_num=models.IntegerField('人数',default=0)
    content=RichTextUploadingField('内容',default='')
    
    def __unicode__(self, ):
        return self.topic

class tb_trends(models.Model):
    title=models.CharField('标题',default='',max_length=100)
    time=models.DateTimeField('时间',default=timezone.now)
    url=models.URLField('链接地址')
    
    def __unicode__(self, ):
        return self.title
    
