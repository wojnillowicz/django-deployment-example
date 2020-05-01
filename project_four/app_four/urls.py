from django.conf.urls import url
from app_four import views

#TEMPLATE NAME
app_name = 'app_four'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other')
]
