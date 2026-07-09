from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def berita(request):
    return render(request, 'berita.html')
