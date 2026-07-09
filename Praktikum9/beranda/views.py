from django.shortcuts import render
from django.http import HttpResponse
from .models import Provinsi,NamaData, Datprof  


def index(request):
    return HttpResponse("Selamat datang di halaman beranda!")


def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html')
# Create your views here.
from .models import Provinsi,NamaData, Datprof
def peta_provinsi(request):
    
    # Ambil semua data provinsi dari database
    data_provinsi = Provinsi.objects.all()
    # Ambil semua data nama data dari database
    data_namadata = NamaData.objects.all()
    return render(request, 'peta_provinsi.html',{
        'data_provinsi': data_provinsi,
        'data_namadata': data_namadata,
    })


def kepadatan_penduduk(request):
    # Ambil semua data kepadatan penduduk dari database
    # data_kepadatan = Datprof.objects.all()
    provinsi = Provinsi.objects.all()
    provinsi_terpilih = request.GET.get('provinsi_terpilih')
    if provinsi_terpilih:
        provinsi_terpilih = int(provinsi_terpilih)
        #data_kepadatan = Datprof.objects.filter(provinsi__id=provinsi_terpilih)
        pass
    
    return render(request, 'kepadatan_penduduk.html', {
        'provinsi': provinsi,
        'provinsi_terpilih': provinsi_terpilih,
    })