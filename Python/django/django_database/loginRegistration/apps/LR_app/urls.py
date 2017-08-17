from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^results/$', views.results),
    url(r'^reg_process$', views.reg_process),
    url(r'^login_process$', views.login_process),
    url(r'^logout/$', views.logout),
]
