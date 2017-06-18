from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^(?P<post_pk>\d+)/$', views.post_comment, name='post_comment'),
]