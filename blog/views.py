from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from .models import *

def index(request):
    try:
        category_list = Category.objects.all()
        articles = Article.objects.all()
        paginator = Paginator(articles, 2)
        ads = Ad.objects.all()
        archive_list = Article.objects.distinct_date()

        try:
            page = int(request.GET.get('page', 1))
            articles = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            articles = paginator.page(1)
    except Exception as e:
        print(e)
    return render(request, 'index.html', locals())

def archive(request):
  try:
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)
    articles = Article.objects.filter(date_publish__contains=year+'-'+month)
    paginator = Paginator(articles, 2)
    try:
      page = int(request.GET.get('page', 1))
      articles = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
      articles = paginator.page(1)

  except Exception as e:
    print(e)
  return render(request, 'archive.html', locals())
