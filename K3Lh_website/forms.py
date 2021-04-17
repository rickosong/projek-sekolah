from django.forms import ModelForm
from django import forms
from K3Lh_website.models import Kotak

class FormKotak(ModelForm):
    class Meta:
        model = Kotak
        fields = '__all__'

        widgets = {
            'lokasi' : forms.TextInput({ 'class' : 'form-control' }),
            'tanggal' : forms.TextInput({ 'class' : 'form-control' }),
            'keadaan' : forms.Select({ 'class' : 'form-control' }),
            'keterangan' : forms.TextInput({ 'class' : 'form-control' }),
        }