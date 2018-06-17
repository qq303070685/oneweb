# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Content
# from .models import User
# from .models import Content, Change, Dfetype
# Register your models here.
class ContentAdmin(admin.ModelAdmin):
	# listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
	list_display = ['date','customer_name','question','author']

	# list_per_page设置每页显示多少条记录，默认是100条
	# list_per_page = 5

	# ordering设置默认排序字段，负号表示降序排序
	# ordering = ('-customer_name',)

	# list_editable 设置默认可编辑字段（name默认不可编辑，因为它是一个链接，点击会进入修改页面）
    #list_editable = ['TEL', 'member_type',]

    # fk_fields 设置显示外键字段
    #fk_fields = ('member_type',)

    # 过滤器功能及能过滤的字段
    # list_filter = ('customer_name',)  
	# list_filter = ['customer_name','question']    

    # 搜索功能及能实现搜索的字段
	# search_fields = ['customer_name','question']
	# pass
	#详细见刘江博客————————定制实例列表页面

# Register your models here.
admin.site.site_header = 'syntax'
admin.site.site_title = 'syntax'
admin.site.register(Content,ContentAdmin)
# admin.site.register(User)
# admin.site.register(Dfetype)
# admin.site.register(Change)