from .models import Article
from django.shortcuts import render, redirect
import requests
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
API_KEY = '6cb28f21ae384e73a91e188613a694ad'
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


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
