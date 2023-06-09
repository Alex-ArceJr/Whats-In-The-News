from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Article, ReadingList
from django.shortcuts import render, redirect
import requests
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ReadingListForm
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
    return render(request, 'article/detail.html', {'technology': technology})


@login_required
def science_article_detail(request, article_id):
    science = Article.objects.get(id=article_id)
    # reading_list = ReadingList.objects.get(id=readinglist_id)
    # print(reading_list)
    return render(request, 'article/science_detail.html', {'science': science})


@login_required
def sports_article_detail(request, article_id):
    sports = Article.objects.get(id=article_id)
    return render(request, 'article/sports_detail.html', {'sports': sports})


@login_required
def entertainment_article_detail(request, article_id):
    entertainment = Article.objects.get(id=article_id)
    return render(request, 'article/entertainment_detail.html', {'entertainment': entertainment})


# @login_required
# def reading_list(request):

#     return render(request, 'article/reading_list.html')

class ReadingListDetail(DetailView):
    model = ReadingList


class ReadingListList(ListView):
    model = ReadingList


class ReadingListCreate(CreateView):
    reading_form = ReadingListForm()
    model = ReadingList
    fields = ['category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# class ReadingListDetail(DetailView):
#     model = ReadingList
#     template_name = 'readinglist/detail.html'
#     context_object_name = 'readinglist'


# class ReadingListList(ListView):
#     model = ReadingList
#     template_name = 'main_app/readinglist_list.html'
#     context_object_name = 'readinglists'


# class ReadingListCreate(CreateView):
#     form_class = ReadingListForm
#     model = ReadingList
#     template_name = 'main_app/readinglist_form.html'
#     success_url = '/readinglist/'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)


# def add_to_reading_list(request, article_id, reading_list_id):
#     article = Article.objects.get(id=article_id)
#     reading_list = ReadingList.objects.get(id=reading_list_id)
#     reading_list.article.add(article)
#     print(reading_list)
#     return redirect(request, 'reading_list.html', {'reading_list': reading_list})
#     # return redirect('reading_list', reading_list_id=reading_list_id)

# def add_to_reading_list(request, article_id, reading_list_id):
#     try:
#         article = Article.objects.get(id=article_id)
#         reading_list = ReadingList.objects.get(id=reading_list_id)
#     except (Article.DoesNotExist, ReadingList.DoesNotExist):
#         # Redirect to a suitable page or handle the case appropriately
#         return redirect('reading_list')
#     reading_list.article.add(article)
#     return redirect('reading_list', reading_list_id=reading_list_id)


class ReadingListUpdate(UpdateView):
    model = ReadingList
    fields = ['category']


class ReadingListDelete(DeleteView):
    model = ReadingList
    success_url = '/readinglist/'
