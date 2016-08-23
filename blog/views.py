import logging
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from .models import *

logger = logging.getLogger('blog.views')

def global_setting(request):
    category_list = Category.objects.all()
    ads = Ad.objects.all()
    tags = Tag.objects.all()
    archive_list = Article.objects.distinct_date()

    return {
        'category_list': category_list,
        'ads': ads,
        'tags': tags,
        'archive_list': archive_list,
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC
    }

def index(request):
    articles = getPage(request, Article.objects.all())
    return render(request, 'index.html', locals())

def archive(request):
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)
    articles = getPage(request, Article.objects.filter(date_publish__contains=year + '-' + month))

    return render(request, 'archive.html', locals())

def getPage(request, articles):
    paginator = Paginator(articles, 2)
    try:
        page = int(request.GET.get('page', 1))
        articles = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        articles = paginator.page(1)
    return articles
