from django.shortcuts import render
from .models import *

def index(request):
    try:
        category_list = Category.objects.all()
        articles = Article.objects.all()
    except Exception as e:
        print(e)
    return render(request, 'index.html', { 'category_list': category_list , 'articles': articles })
