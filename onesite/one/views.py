# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from forms import UserForm,ContentForm
from models import Content,User
from django.contrib.auth import authenticate,login ,logout
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from xlwt import *
import StringIO
# from django.contrib.auth.models import User

# Create your views here.
def login_dl(request):

	if  request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'GET':
			login_form = UserForm()

		if request.method == 'POST':
			login_form = UserForm(request.POST)
			if login_form.is_valid():
				username = login_form.cleaned_data['username']
				password = login_form.cleaned_data['password']
				user = authenticate(username=username,password=password)
				print 111111
				print username
				print password
				if user:
					print 222222
					login(request,user)
					print 333333
					return redirect('index')
				else:
					return redirect('https://www.baidu.com/')
		return render(request,'login.html',locals())

def index(request):
	# if request.user.is_authenticated:
	# 	print request.user.username
	# 	print request.session.get('is_login',None)
	# 	# return render(request,'jihua/ribao.html',locals())
	# 	content = Content.objects.all()
	# 	print content.customer_name 
	# 	print content.question
	# else:
	# 	return redirect('login_dl')
	if request.user.is_authenticated:
		if request.user.username == 'admin':
			content = Content.objects.all()
		else:
			content = Content.objects.filter(author__username=request.user)
			print request.user
		paginator = Paginator(content,10) #2是指一页中有多少条数据

		page = request.GET.get('page')
		try:
			content = paginator.page(page)

		except PageNotAnInteger:
			content = paginator.page(1)

		except EmptyPage:
			content = paginator.page(paginator.num_pages)



		return render(request,'jihua/ribao.html',locals())
	else:
		return redirect('login_dl')

def tiaozhuan(request):
	return redirect('login_dl')

def logout_tc(request):
	logout(request)
	return redirect('login_dl')

def delete(request,pk):
	# id = request.GET.get('pk')
	content = Content.objects.get(id=pk)
	content.delete()
	print '1111111'
	print content

	return redirect('index')

def viewcontent(request,pk):
	content = Content.objects.get(id=pk)
	print content.question

	return render(request,'jihua/content.html',locals())

def create(request):
	if request.method == 'GET':
		new = ContentForm()
	if request.method == 'POST':
		new = ContentForm(request.POST)
		print new.is_valid()

		if new.is_valid():#如果is_valid()不对可以打印new.errors来看哪块有问题,可以搜form组件is_valid校验机制
			date = new.cleaned_data['date']
			customer_name = new.cleaned_data['customer_name']
			dfe_name = new.cleaned_data['dfe_name']
			question = new.cleaned_data['question']
			solution = new.cleaned_data['solution']
			solution_or_not = new.cleaned_data['solution_or_not']
			update_or_not = new.cleaned_data['update_or_not']
			change_or_not = new.cleaned_data['change_or_not']
			share_or_not = new.cleaned_data['share_or_not']
			# author = request.user.username
			print request.user

			# aa = {}
			# aa.update(new.cleaned_data)
			# aa['author'] = author
			aa = Content()
			aa.date = date
			aa.customer_name = customer_name
			aa.dfe_name = dfe_name
			aa.question = question
			aa.solution = solution
			aa.solution_or_not = solution_or_not
			aa.update_or_not = update_or_not
			aa.change_or_not = change_or_not
			aa.share_or_not = share_or_not
			aa.author = request.user
			aa.save()

			return redirect('index')
		else:
			print 'ccccc'
			for i in new.errors:
				print i


	return render(request,'jihua/input.html',locals())

def edit(request,pk):
	content = Content.objects.get(pk=pk)
	print content.customer_name
	if request.method == 'POST':
		print 'okokok!'
		form = ContentForm(request.POST,instance=content)
		if form.is_valid():
			form.save()
		return redirect('index')
	else:
		print 'errors!!!!'
		new_content = ContentForm(instance=content)
	return render(request,'jihua/edit.html',locals())

def search(request):
	q = request.GET.get('q','aaa')
	print type(q)
	error_msg = ''

	if not q:
		error_msg = 'qingshuru!'
		print 'errors'
	else:
		print 'ok'

	search_list = Content.objects.filter(Q(question__icontains=q) | Q(customer_name__icontains=q) | Q(solution__icontains=q)| Q(author__username=q))
	return render(request,'jihua/search.html',locals())

def download_excel(request):
	# time_start = request.GET.get('time_start',None)
	# time_end = request.GET.get('time_end',None)
	# #__gte大于等于 __lte小于等于
	# if time_end and time_end:
	# 	content = Content.objects.filter(date__gte=time_start).filter(date__lte=time_end)
	content = Content.objects.filter(question='123')
	if content:
		ws = Workbook(encoding='utf-8')
		w = ws.add_sheet(u'one')
		w.write(0,0,u'客户名称')
		w.write(0,1,u'question')
		w.write(0,2,u'solution')
		excel_row = 1
		for i in content:
			customer_name = i.customer_name
			question = i.question
			solution = i.solution
			w.write(excel_row,0,customer_name)
			w.write(excel_row,1,question)
			w.write(excel_row,2,solution)
			excel_row +=1
		# sio = StringIO.StringIO()
		# ws.save(sio)
		# # sio.seek(0)
		response = HttpResponse(content_type='application/msexcel')
		response['Content-Disposition'] = 'attachment; filename=example.xls'
		ws.save(response)
		return response


	else:
		render(request,'jihua/content.html',locals())





# def login(request):
# 	if request.session.get('is_login',None):
# 		return redirect('/admin/')
# 	else:
# 		if request.method =='POST':
# 			login_form = UserForm(request.POST)
# 			session_save = request.POST.getlist('saved')
# 			# print session_save
# 			if login_form.is_valid():
# 				username = login_form.cleaned_data['username']
# 				password = login_form.cleaned_data['password']
# 				try:
# 					# user = User.objects.get(name=username)
# 					user = authenticate(username=username,password=password)

# 					print username
# 					# print user.password
# 					# if user.password == password:
# 					if user:
# 						# if session_save :
# 						# 	request.session['is_login'] = True
# 						# 	request.session['user_id'] = user.id
# 						# 	request.session['user_name'] = user.name
# 						# 	print 'sesion saved!'
# 						# return render(request,'jihua/ribao.html',locals())
# 						login(request,user)
# 						return redirect(to='index')
# 					else:
# 						return redirect('https://www.baidu.com/')

# 				except:
# 					print 'meiyou zhege yonghu !'
# 					return render(request,'jihua/ribao.html',locals())
# 		else:
# 			login_form = UserForm()

# 		return render(request,'login.html',locals())


# def logout(request):
# 	if not request.session.get('is_login',None):
# 		print 555555
# 		return redirect('/login/')

# 	request.session.flush()
# 	return redirect('/login/')

# def tiaozhuan(request):
# 	return redirect('/login/')

# def index(request):
# 	# ribao_list = Content.objects.all().order_by('date')
# 	ribao_list = 1111
# 	print ribao_list
# 	print request.session.get('is_login',None)
# 	print request.user.is_authenticated()
# 	print dir(request.session)
# 	print request.user.username
# 	print ribao_list
	
# 	return render(request,'jihua/ribao.html',context={'ribao_list':ribao_list})

