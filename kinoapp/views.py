from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'kinoapp/index.html')

def blog(request):
    return render(request, 'kinoapp/blog.html')