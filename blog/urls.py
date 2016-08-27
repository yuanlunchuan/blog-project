from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^article/$', article, name='article'),
    url(r'^archive/', archive, name='archive'),
    url(r'^reg', do_reg, name='reg'),
    url(r'^logout$', do_logout, name='logout'),
    url(r'^login', do_login, name='login'),
    url(r'^comment/post/$', comment_post, name='comment_post'),
]
