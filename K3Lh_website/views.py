from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'loginpage.html')

def home(request):
    return render(request, 'home.html')