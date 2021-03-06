"""lectura_ciclica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from clase.views import vista, crear_comentario
from django.contrib.auth import views

urlpatterns = [
    url(r'^$', vista, name="home"),
    url(r'^crear_comentario/(?P<pk>\d+)$',
        crear_comentario, name="crear_comentario"),
    # url(r'^listar_comentario/(?P<pk>\d+)$', listar_comentario, name="listar_comentario"),
    url(r'^admin/', admin.site.urls),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^login/$', views.login),
    url(r'^site_logout/$', views.logout),
]
