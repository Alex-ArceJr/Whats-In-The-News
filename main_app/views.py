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

    return render(request, 'sports.html', {
        'articles': articles
    })


def science(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    return render(request, 'science.html', {
        'articles': articles
    })


def entertainment(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    return render(request, 'entertainment.html', {
        'articles': articles
    })


def technology(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    return render(request, 'technology.html', {
        'articles': articles
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
