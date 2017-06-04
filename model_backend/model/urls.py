from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/(.*)', views.show, name='show'),
    url(r'^token', views.token, name='token')
]
