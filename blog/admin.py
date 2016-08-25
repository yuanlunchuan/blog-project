from django.contrib import admin

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'content', )
    list_display_links = ('title', 'desc', 'content',)
    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user', 'tag',)
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend', )
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'article', 'date_publish', )

class AdAdmin(admin.ModelAdmin):
    list_display = ('description', 'date_publish', )

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Links)
admin.site.register(Ad, AdAdmin)
