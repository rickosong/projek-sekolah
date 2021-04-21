from django.contrib import admin
from K3Lh_website.models import *

# Register your models here.
class KotakAdmin(admin.ModelAdmin):
    list_display = ['lokasi', 'tanggal', 'keadaan', 'keterangan']
    search_fields =  ['lokasi', 'tanggal', 'keadaan']
    list_filter = ('keadaan',)
    list_per_page = 5

admin.site.register(Kotak, KotakAdmin)
admin.site.register(Keadaan)
admin.site.register(Jabatan)
admin.site.register(Pengguna)