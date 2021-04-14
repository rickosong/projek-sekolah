from django.forms import ModelForm
from django import forms
from K3Lh_website.models import Kotak

class FormKotak(ModelForm):
    class Meta:
        model = Kotak
        fields = '__all__'

        widgets = {
            'lokasi' : forms.TextInput({ 'class' : 'form-cotrol' }),
            'tanggal' : forms.TextInput({ 'class' : 'form-cotrol' }),
            'keadaan' : forms.Select({ 'class' : 'form-cotrol' }),
            'keterangan' : forms.TextInput({ 'class' : 'form-cotrol' }),
        }