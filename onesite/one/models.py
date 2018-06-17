# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from ckeditor.fields import RichTextUploadingField

# Create your models here.
# class User(models.Model):
# 	name = models.CharField(max_length=100)
# 	password = models.CharField(max_length=100)
# 	c_time = models.DateField(auto_now=True)

# 	def __unicode__(self):
# 		# return models.Model.__unicode__(self)
# 		return self.name

# 	class Meta:
# 		ordering = ['name']
# 		verbose_name = "用户"
# 		verbose_name_plural = "用户"		

#第一种方式：
class Content(models.Model):
	dfe_choices = (
			('Pro','Pro'),
			('Esko','Esko'),
			('PM','PM'),
			('无','无'),
		)
	change_choices = (
			('无','无'),
			('库房申请','库房申请'),
			('小库申请','小库申请'),
			('HP提供','HP提供'),
			('第三方购买','第三方购买'),
		)
	date = models.DateField()
	customer_name = models.CharField(max_length=255,editable=True,null=False)
	# editable=True 在admin中可以编辑(默认都是可以编辑的)   null数据库字段是否可以为空
	dfe_name = models.CharField(max_length=255,choices=dfe_choices,default='Pro')
	# CharField 可以用ChoiceField替换
	question = models.CharField(max_length=255,unique=False,verbose_name='问题描述') 
	# unique=True 不能重复的意思  verbose_name admin中的字段名称 
	solution = models.TextField()
	solution_or_not = models.BooleanField(default=True)
	update_or_not = models.BooleanField(default=True)
	change_or_not = models.CharField(max_length=255,choices=change_choices,default='无')
	# dfe_choices也可以这样写
	share_or_not = models.BooleanField(default=True)#huo yong required=False
	author = models.ForeignKey(User,null=True)
	


	def __unicode__(self):
		return self.customer_name

	class Meta:
		ordering = ['-date','-author']
		verbose_name = "日报"
		verbose_name_plural = "日报"


# # 第二种方式：
# class Dfetype(models.Model):
# 	dfename = models.CharField(max_length=100,null=False)

# 	def __unicode__(self):
# 		return self.dfename

# class Change(models.Model):
# 	changename = models.CharField(max_length=100,null=False)

# 	def __unicode__(self):
# 		return self.changename

# class Content(models.Model):
# 	date = models.DateField(auto_now=True)
# 	customer_name = models.CharField(max_length=255,editable=True,null=False)
# 	dfe_name = models.ForeignKey(Dfetype,editable=True)
# 	question = models.CharField(max_length=255,unique=True,verbose_name='问题描述')  
# 	solution = models.TextField()
# 	solution_or_not = models.BooleanField(default=True)
# 	update_or_not = models.BooleanField(default=True)
# 	change_or_not = models.ForeignKey(Change)
# 	share_or_not = models.BooleanField(default=True)
# 	author = models.ForeignKey(User,null=False)	

# 	def __unicode__(self):
# 		return self.customer_name
