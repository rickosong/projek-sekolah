from django.shortcuts import render, redirect
from K3Lh_website.models import *
from K3Lh_website.forms import FormPendataan
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from K3Lh_website.decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, 'Ada kesalahan dalam Username atau Password Anda')

    konteks = {}
    return render(request, 'loginpage.html', konteks)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def serbaserbi(request):
    return render(request, 'serbaserbi.html')

@login_required(login_url='login')
def p3k(request):

    form = FormPendataan()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = FormPendataan(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hasil/')

    konteks= {'form':form}
    return render(request, 'p3k.html', konteks)

@login_required(login_url='login')
def edit(request, pk):
    box = Pendataan.objects.get(id=pk)
    form = FormPendataan(instance=box)
    if request.method == 'POST':
        form = FormPendataan(request.POST, instance=box)
        if form.is_valid():
            form.save()
            return redirect('/hasil/')

    konteks = {'form':form}
    return render(request, 'p3k.html', konteks)

@login_required(login_url='login')
def hasil(request):
    box = Pendataan.objects.all()

    konteks = {
        'box' : box,
    }

    return render(request, 'hasill.html', konteks)

@login_required(login_url='login')
def hapus(request, pk):
    box = Pendataan.objects.get(id=pk)
    if request.method == 'POST':
        box.delete()
        return redirect('/hasil/')
        
    konteks = {'item':box}
    return render(request, 'hapus.html', konteks)

@login_required(login_url='login')
def profil(request):
    return render(request, 'Profil.html')