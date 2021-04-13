from django.db import models

# Create your models here.
class Keadaan(models.Model):
    jenis = models.CharField(max_length = 40)

    def __str__(self):
        return self.jenis

class Kotak(models.Model):
    lokasi = models.CharField(max_length = 90)
    tanggal = models.CharField(max_length = 35)
    keadaan = models.ForeignKey(Keadaan, on_delete = models.CASCADE, null = True)
    keterangan = models.TextField(blank = True)

    def __str__(self):
        return self.lokasi