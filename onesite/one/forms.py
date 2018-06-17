# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm,Textarea,Select,DateInput
from .models import Content



class UserForm(forms.Form):
	username = forms.CharField(label='用户名',max_length=100,widget=forms.TextInput(attrs={'placeholder':u'请输入用户名'}))
	password = forms.CharField(label='密码',max_length=100,widget=forms.PasswordInput(attrs={'placeholder':u'请输入密码'}))
#widget=forms.TextInput(attrs={'class': "form-control",  'placeholder': u'手机号码'}),也可以这样

class ContentForm(ModelForm):

	class Meta:
		model = Content
		# fields = ['date','customer_name','question']
		#fields = '__all__'    这样就全显示
		#exclude = ['date']   不包括这里面的内容
		exclude = ['author']
		# fields = '__all__'
		widgets = {
					'date' : DateInput(attrs={'type':'text','font-size':'20px'}),#这样不会出现选择日期栏
					# 'date' : Text
					'dfe_name' : Select(attrs={'class':'dfetype'}),
					#上面的就是直接引用css中的样式
					'question' : Textarea(attrs={"rows":2 ,"cols":120}),
					'solution' : Textarea(attrs={"rows":8 ,"cols":120}),
					# 'author':Textarea(attrs={'style':'display'}),

		}

