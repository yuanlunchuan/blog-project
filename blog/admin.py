from django.contrib import admin

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'content',)
    list_display_links = ('title', 'desc', 'content',)
    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend', )
        }),
    )

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)