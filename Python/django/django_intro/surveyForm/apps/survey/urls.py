from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index), #survey
    url(r'^survey/process$', views.process),
    url(r'^results$', views.results),
]
