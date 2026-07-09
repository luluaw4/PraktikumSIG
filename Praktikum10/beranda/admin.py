from django.contrib import admin

# Register your models here.
from .models import Kelurahan, Kabkota, Kecamatan, Provinsi
#admin.site.register(Provinsi)
@admin.register(Provinsi)  # 3. Gunakan decorator untuk mendaftarkan model
class ProvinsiAdmin(admin.ModelAdmin):
    # Kolom apa saja yang mau ditampilkan di list halaman admin
    list_display = ('id', 'name', 'alt_name', 'latitude', 'longitude')
 
    search_fields = ('name', 'alt_name')  # Kolom yang bisa dicari

    list_filter = ('name',)  # Kolom yang bisa difilter

@admin.register(Kabkota)  # 3. Gunakan decorator untuk mendaftarkan model
class KabkotaAdmin(admin.ModelAdmin):
    # Kolom apa saja yang mau ditampilkan di list halaman admin
    list_display = ('id', 'name', 'alt_name', 'latitude', 'longitude')
 
    search_fields = ('name', 'alt_name')  # Kolom yang bisa dicari

    list_filter = ('name',)
    
@admin.register(Kecamatan)  # 3. Gunakan decorator untuk mendaftarkan model
class KecamatanAdmin(admin.ModelAdmin):
    # Kolom apa saja yang mau ditampilkan di list halaman admin
    list_display = ('id', 'name', 'alt_name', 'latitude', 'longitude')
 
    search_fields = ('name', 'alt_name')  # Kolom yang bisa dicari

    list_filter = ('name',)   # Kolom yang bisa difilter

@admin.register(Kelurahan)  # 3. Gunakan decorator untuk mendaftarkan model
class KelurahanAdmin(admin.ModelAdmin):
    # Kolom apa saja yang mau ditampilkan di list halaman admin
    list_display = ('id', 'name', 'alt_name', 'latitude', 'longitude')
 
    search_fields = ('name', 'alt_name')  # Kolom yang bisa dicari

    list_filter = ('name',)   # Kolom yang bisa difilter

from .models import NamaData, Datprof
@admin.register(NamaData)
class NamaDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama')
    search_fields = ('nama',)


@admin.register(Datprof)
class DatprofAdmin(admin.ModelAdmin):
    list_display = ('id', 'provinsi', 'namadata', 'tahun', 'jumlah')
    search_fields = ('provinsi__name', 'namadata__nama', '=tahun')
    list_filter = ('tahun', 'namadata')