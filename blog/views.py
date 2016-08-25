import logging
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from .models import *
from django.db.models import Count
from blog.forms import *

logger = logging.getLogger('blog.views')

def global_setting(request):
    category_list = Category.objects.all()
    ads = Ad.objects.all()
    tags = Tag.objects.all()
    archive_list = Article.objects.distinct_date()
    comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    comment_list = [Article.objects.get(pk=comment_count['article']) for comment_count in comment_count_list]
    click_article_list = Article.objects.all().order_by('-click_count')
    command_articles = Article.objects.filter(is_recommend=True)
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC

    return locals()

def index(request):
    articles = getPage(request, Article.objects.all())
    return render(request, 'index.html', locals())

def archive(request):
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)
    articles = getPage(request, Article.objects.filter(date_publish__contains=year + '-' + month))
    return render(request, 'archive.html', locals())

def do_logout(request):
  pass

def comment_post(request):
  pass

def article(request):
    try:
        id = request.GET.get('id', None)
        try:
            article = Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return render(request, 'failure.html', {'reason': '没有找到对应的文章'})

        comment_form = CommentForm({'author': request.user.username,
                                    'email': request.user.email,
                                    'url': request.user.url,
                                    'article': id} if request.user.is_authenticated() else{'article': id})

        comments = Comment.objects.filter(article=article).order_by('id')
        comment_list = []
        for comment in comments:
            for item in comment_list:
                if not hasattr(item, 'children_comment'):
                    setattr(item, 'children_comment', [])
                if comment.pid == item:
                    item.children_comment.append(comment)
                    break
            if comment.pid is None:
                comment_list.append(comment)
    except Exception as e:
      logger.error(e)
    return render(request, 'article.html', locals())

def comment_post(request):
    try:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment.objects.create(username=comment_form.cleaned_data["author"],
                                             email=comment_form.cleaned_data["email"],
                                             url=comment_form.cleaned_data["url"],
                                             content=comment_form.cleaned_data["comment"],
                                             article_id=comment_form.cleaned_data["article"],
                                             user=request.user if request.user.is_authenticated() else None)
            comment.save()
        else:
            return render(request, 'failure.html', {'reason': comment_form.errors})
    except Exception as e:
        logger.error(e)
    return redirect(request.META['HTTP_REFERER'])

def getPage(request, articles):
    paginator = Paginator(articles, 2)
    try:
        page = int(request.GET.get('page', 1))
        articles = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        articles = paginator.page(1)
    return articles
