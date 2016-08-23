from django.conf.urls import url
from blog.views import index, archive

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^archive/', archive, name='archive'),
]

