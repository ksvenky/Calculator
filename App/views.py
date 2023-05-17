from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def authors(request):
    return render(request, 'authors.html', {})

def scientific_calculator(request):
    return render(request, 'sc.html', {})

