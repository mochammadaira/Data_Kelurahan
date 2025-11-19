from django.contrib import admin
from .models import Warga, Pengaduan # Tambahkan Pengaduan

admin.site.register(Warga)
admin.site.register(Pengaduan) # Daftarkan model baru