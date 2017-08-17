from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg_process$', views.reg_process),
    url(r'^success/$', views.success),
    url(r'^logout/$', views.logout),
]
