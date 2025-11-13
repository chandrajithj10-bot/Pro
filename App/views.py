from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def letter(request):
    return render(request, 'letter.html')
