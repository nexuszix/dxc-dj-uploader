from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^list/$', views.render_list, name='list'),
    url(r'^upload/$', views.upload, name='upload'),
]