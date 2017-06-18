from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$',views.about, name='about'),
    url(r'^post/(?P<pk>\d+)', views.PostDetailView.as_view(), name='detail'),
    url(r'^archive/$', views.ArchiveView.as_view(), name='archive'),
    url(r'^category/(?P<pk>\d+)', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>\d+)',views.TagView.as_view(),name='tag')
]