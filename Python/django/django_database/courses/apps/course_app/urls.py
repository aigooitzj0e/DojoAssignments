from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg_process$', views.reg_process),
    url(r'^login_process$', views.login_process),
    url(r'^dashboard/$', views.dashboard),
    url(r'^logout/$', views.logout),
    url(r'^teach/$', views.teach),
    url(r'^teach_process/(?P<id>\d+)$', views.teach_process),
    url(r'^enroll/$', views.enroll),
    url(r'^enroll_process/(?P<cid>\d+)$', views.enroll_process),
    url(r'^dashboard/delete/(?P<id>\d+)$',views.delete)
]
