from django.contrib import admin

from .models import *
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)

