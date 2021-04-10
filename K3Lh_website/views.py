from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'loginpage.html')

def home(request):
    return render(request, 'home.html')

def serbaserbi(request):
    return render(request, 'serbaserbi.html')

def pendataan(request):
    return render(request, 'pendataan.html')

def p3k(request):
    return render(request, 'p3k.html')

def hasil(request):
    return render(request, 'hasil.html')

def profil(request):
    return render(request, 'profil.html')