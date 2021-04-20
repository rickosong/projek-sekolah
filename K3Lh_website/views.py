from django.shortcuts import render, redirect
from K3Lh_website.models import Kotak
from K3Lh_website.forms import FormKotak

# Create your views here.
def login(request):
    return render(request, 'loginpage.html')

def home(request):
    return render(request, 'home.html')

def serbaserbi(request):
    return render(request, 'serbaserbi.html')

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

def hasil(request):
    box = Kotak.objects.all()

    konteks = {
        'box' : box,
    }

    return render(request, 'hasill.html', konteks)

def hapus(request, pk):
    box = Kotak.objects.get(id=pk)
    if request.method == 'POST':
        box.delete()
        return redirect('/hasil/')
        
    konteks = {'item':box}
    return render(request, 'hapus.html', konteks)

def profil(request):
    return render(request, 'profil.html')