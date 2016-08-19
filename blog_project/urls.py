from django.conf.urls import url
from django.contrib import admin
from blog.views import index
from django.conf import settings

urlpatterns = [
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
]
