"""WEB9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from siteAC import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^prof/$', views.Prof.as_view(), name='prof'), 
    #ao chamar da VIEW, sempre usar as.view() para realizar o import do que você estiver chamando
    url(r'^aluno/$', views.Aluno.as_view(), name='aluno'),
    url(r'^disci/$', views.Disc.as_view(), name='disci'),
]