from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from .models import *

def index(request):
    try:
        category_list = Category.objects.all()
        articles = Article.objects.all()
        paginator = Paginator(articles, 2)
        try:
            page = 1
            if request.GET.get('page'):
                page = int(request.GET.get('page'))
            articles = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            articles = paginator.page(1)
    except Exception as e:
        print(e)
    return render(request, 'index.html', locals())
