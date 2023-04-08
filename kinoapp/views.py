from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'index',
    }
    return render(request, 'kinoapp/index.html', context)

def blog(request):
    context = {
        'title':'blog',
    }
    return render(request, 'kinoapp/blog.html',context)