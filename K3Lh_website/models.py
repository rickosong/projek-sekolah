from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Keadaan(models.Model):
    jenis_keadaan = models.CharField(max_length=40)

    def __str__(self):
        return self.jenis_keadaan

class Pendataan(models.Model):
    lokasi = models.CharField(max_length=90)
    tanggal = models.CharField(max_length=35)
    keadaan = models.ForeignKey(Keadaan, on_delete = models.CASCADE, null=True)
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return self.lokasi

class Jabatan(models.Model):
    jabat = models.CharField(max_length=60)

    def __str__(self):
        return self.jabat

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100, null =True)
    NIK = models.CharField(max_length=30, null=True)
    jabatan = models.ForeignKey(Jabatan, on_delete = models.CASCADE, null=True)
    nomor = models.CharField(max_length=12, null=True)
    alamat = models.CharField(max_length=300, null=True)
    image = models.ImageField(default='Gambarprofil.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


