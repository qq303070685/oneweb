"""onesite URL Configuration

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
from one import views
from django.views import static
from one.uploads import upload_image
from django.conf import settings
# from django.contrib.auth import logout


app_name = 'one'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.tiaozhuan ,name='login_dl'),
    url(r'^login/$', views.login_dl ,name='login_dl'),
    # url(r'^logout/$', views.logout ,name='logout'),
    url(r'^index/$', views.index ,name='index'),
    url(r'^logout/$',views.logout_tc ,name='logout'),
    url(r'^index/(\d+)$',views.delete ,name='delete'),
    url(r'^content/(\d+)$',views.viewcontent ,name='viewcontent'),
    url(r'^new/$',views.create ,name='create'),
    url(r'^edit/(\d+)$',views.edit ,name='edit'),
    url(r'^search/$',views.search ,name='search'),
    url(r'^uploads/(?P<path>.*)$',static.serve,{'document_root':settings.MEDIA_ROOT},),
    url(r'^upload/(?P<dir_name>[^/]+)$',upload_image,name='upload_image'),
    url(r'^download/$',views.download_excel,name='download_excel'),
    # url(r'^ckeditor/',include('ckeditor_uploader.urls')),
]