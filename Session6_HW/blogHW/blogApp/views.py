from django.shortcuts import render, redirect
from .models import Article
import time

# Create your views here.
def index(request):
    movies_total = Article.objects.filter(category="movie").count()
    dramas_total = Article.objects.filter(category="drama").count()
    programmings_total = Article.objects.filter(category="programming").count()
    return render(request, 'index.html', {'movies_total': movies_total, 'dramas_total': dramas_total, 'programmings_total': programmings_total})

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    return render(request, 'detail.html', {'article': article})

def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            written_time = time.ctime()
        )
        return redirect('detail', article_pk=new_article.pk)
    return render(request, 'new.html')

def movie(request):
    movies = Article.objects.filter(category="movie")
    return render(request, 'movie.html', {'articles': movies})

def drama(request):
    dramas = Article.objects.filter(category="drama")
    return render(request, 'drama.html', {'articles': dramas})

def programming(request):
    programmings = Article.objects.filter(category="programming")
    return render(request, 'programming.html', {'articles': programmings})