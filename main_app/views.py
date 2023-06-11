from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Article, ReadingList
from django.shortcuts import render, redirect
import requests
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ReadingListForm
from django.contrib.auth.mixins import LoginRequiredMixin
API_KEY = '6cb28f21ae384e73a91e188613a694ad'
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def sports(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    for article in articles:
        if not Article.objects.filter(url=article['url']).exists():
            Article.objects.create(
                author=article['author'] or 'author not listed',
                title=article['title'],
                description=article['description'] or '',
                url=article['url'],
                urlImage=article['urlToImage'] or '',
                category='sports'
            )

    sportsArticles = Article.objects.filter(category__icontains='sports')

    return render(request, 'sports.html', {
        'articles': sportsArticles
    })


@login_required
def science(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    for article in articles:
        if not Article.objects.filter(url=article['url']).exists():
            Article.objects.create(
                author=article['author'] or 'author not listed',
                title=article['title'],
                description=article['description'] or '',
                url=article['url'],
                urlImage=article['urlToImage'] or '',
                category='science'
            )
    scienceArticles = Article.objects.filter(category__icontains='science')

    return render(request, 'science.html', {
        'articles': scienceArticles
    })


@login_required
def entertainment(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    for article in articles:
        if not Article.objects.filter(url=article['url']).exists():
            Article.objects.create(
                author=article['author'] or 'author not listed',
                title=article['title'],
                description=article['description'] or '',
                url=article['url'],
                urlImage=article['urlToImage'] or '',
                category='entertainment'
            )

    entertainmentArticles = Article.objects.filter(
        category__icontains='entertainment')

    return render(request, 'entertainment.html', {
        'articles': entertainmentArticles
    })


@login_required
def technology(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    for article in articles:
        if not Article.objects.filter(url=article['url']).exists():
            Article.objects.create(
                author=article['author'] or 'author not listed',
                title=article['title'],
                description=article['description'] or '',
                url=article['url'],
                urlImage=article['urlToImage'] or '',
                category='technology'
            )

    technologyArticles = Article.objects.filter(
        category__icontains='technology')

    return render(request, 'technology.html', {
        'articles': technologyArticles
    })


def signup(request):
    # POST request
    error_message = ''
    # user is signing up with a form submission
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')
        else:
            error_message = 'invalid signup - try again'
    # GET request
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error': error_message
    })


@login_required
def technology_article_detail(request, article_id):
    technology = Article.objects.get(id=article_id)
    reading_form = ReadingListForm()
    return render(request, 'article/detail.html', {'technology': technology, 'reading_form': reading_form})


@login_required
def science_article_detail(request, article_id):
    science = Article.objects.get(id=article_id)
    reading_form = ReadingListForm()
    return render(request, 'article/science_detail.html', {'science': science, 'reading_form': reading_form})


@login_required
def sports_article_detail(request, article_id):
    sports = Article.objects.get(id=article_id)
    reading_form = ReadingListForm()
    return render(request, 'article/sports_detail.html', {'sports': sports, 'reading_form': reading_form})


@login_required
def entertainment_article_detail(request, article_id):
    entertainment = Article.objects.get(id=article_id)
    reading_form = ReadingListForm()
    return render(request, 'article/entertainment_detail.html', {'entertainment': entertainment, 'reading_form': reading_form})


class ReadingListDetail(LoginRequiredMixin, DetailView):
    model = ReadingList


def readingListIndex(request):

    models = ReadingList.objects.all()
    return render(request, 'main_app/readinglist_list.html', {'models': models})


class ReadingListCreate(LoginRequiredMixin, CreateView):
    reading_form = ReadingListForm()
    model = ReadingList
    template_name = 'main_app/readinglist_form.html'
    fields = ['category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReadingListUpdate(LoginRequiredMixin, UpdateView):
    model = ReadingList
    fields = ['category']


class ReadingListDelete(LoginRequiredMixin, DeleteView):
    model = ReadingList
    success_url = '/readinglist/'
