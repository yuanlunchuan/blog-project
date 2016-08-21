from django.conf.urls import url
from django.contrib import admin
from blog.views import index, archive
from django.conf import settings

#url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^archive/', archive, name='archive'),
]
