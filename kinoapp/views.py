from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    context = {
        'title':'index',
    }
    return render(request, 'kinoapp/index.html', context)

def blog(request):
    rows = OurBlog.objects.all()

    context = {
        'title':'blog',
        'rows': rows
    }

    return render(request, 'kinoapp/blog.html',context)

def news(request):

    rows = News.objects.all()

    context = {
        'title':'news',
        'rows': rows,
    }

    return render(request, 'kinoapp/news.html',context)

def newsDetails(request, id):

    rows = NewsDetails.objects.filter(newsObject__id=id)

    context = {
        'title':'news',
        'rows': rows,
    }

    return render(request, 'kinoapp/blog-details.html',context)