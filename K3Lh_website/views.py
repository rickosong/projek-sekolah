from django.shortcuts import render, redirect
from K3Lh_website.models import Kotak, Pengguna
from K3Lh_website.forms import FormKotak
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
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

    form = FormKotak()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = FormKotak(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hasil/')

    konteks= {'form':form}
    return render(request, 'p3k.html', konteks)

@login_required(login_url='login')
def edit(request, pk):
    box = Kotak.objects.get(id=pk)
    form = FormKotak(instance=box)
    if request.method == 'POST':
        form = FormKotak(request.POST, instance=box)
        if form.is_valid():
            form.save()
            return redirect('/hasil/')

    konteks = {'form':form}
    return render(request, 'p3k.html', konteks)

@login_required(login_url='login')
def hasil(request):
    box = Kotak.objects.all()

    konteks = {
        'box' : box,
    }

    return render(request, 'hasill.html', konteks)

@login_required(login_url='login')
def hapus(request, pk):
    box = Kotak.objects.get(id=pk)
    if request.method == 'POST':
        box.delete()
        return redirect('/hasil/')
        
    konteks = {'item':box}
    return render(request, 'hapus.html', konteks)

@login_required(login_url='login')
def profil(request):
    pengguna = Pengguna.objects.all()

    konteks = {'pengguna':pengguna}
    return render(request, 'Profil.html', konteks)