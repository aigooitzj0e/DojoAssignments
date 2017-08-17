from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^new_process$',views.new_process),
    url(r'^edit/(?P<idd>\d+)$', views.edit),
    url(r'^edit_process/(?P<idd>\d+)$', views.edit_process),
    url(r'^show/(?P<idd>\d+)$', views.show),
    url(r'^delete/(?P<idd>\d+)$', views.delete),
]
