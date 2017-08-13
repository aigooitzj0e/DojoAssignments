from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index), #random_app
    url(r'^generate/$', views.generate),
    url(r'^reset/$', views.reset),
]
