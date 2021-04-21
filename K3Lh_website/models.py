from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Keadaan(models.Model):
    jenis = models.CharField(max_length=40)

    def __str__(self):
        return self.jenis

class Kotak(models.Model):
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

class Pengguna(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100, null =True)
    NIK = models.CharField(max_length=30, null=True)
    jabatan = models.ForeignKey(Jabatan, on_delete = models.CASCADE, null=True)
    nomor = models.CharField(max_length=12, null=True)
    alamat = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.nama


