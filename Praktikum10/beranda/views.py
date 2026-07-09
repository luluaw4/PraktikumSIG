import json

from django.shortcuts import render
from django.http import HttpResponse
from .models import Provinsi, NamaData, Datprof


def index(request):
    return HttpResponse("Selamat datang di halaman beranda!")


def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html')
# Create your views here.
def peta_provinsi(request):
    # Ambil semua data provinsi dari database
    data_provinsi = Provinsi.objects.all()
    # Ambil semua data nama data dari database
    data_namadata = NamaData.objects.all()
    selected_nama_data = request.GET.get('nama_data', '')
    selected_nama_data_name = ''
    province_data_list = []

    selected_namadata_obj = None
    if selected_nama_data:
        selected_namadata_obj = NamaData.objects.filter(id=selected_nama_data).first()
        if selected_namadata_obj:
            selected_nama_data_name = selected_namadata_obj.nama

    for prov in data_provinsi:
        datprof_items = []
        if selected_namadata_obj:
            datprof_items = list(
                Datprof.objects.filter(provinsi=prov, namadata=selected_namadata_obj)
                .order_by('tahun')
                .values('tahun', 'jumlah')
            )
        province_data_list.append({
            'provinsi': prov,
            'datprof_items': datprof_items,
        })

    return render(request, 'peta_provinsi.html', {
        'data_provinsi': data_provinsi,
        'province_data_list': province_data_list,
        'data_namadata': data_namadata,
        'selected_nama_data': selected_nama_data,
        'selected_nama_data_name': selected_nama_data_name,
    })


def kepadatan_penduduk(request):
    # Ambil semua data kepadatan penduduk dari database
    # data_kepadatan = Datprof.objects.all()
    provinsi = Provinsi.objects.all()
    data_namadata = NamaData.objects.all()
    provinsi_terpilih = request.GET.get('provinsi_terpilih', '')
    selected_nama_data = request.GET.get('nama_data', '')
    selected_nama_data_name = ''

    selected_provinsi = None
    datprof_list = []

    if selected_nama_data:
        selected_nama_data_name = NamaData.objects.filter(id=selected_nama_data).values_list('nama', flat=True).first() or ''

    try:
        if provinsi_terpilih:
            provinsi_id = int(provinsi_terpilih)
            selected_provinsi = Provinsi.objects.filter(id=provinsi_id).first()
            if selected_provinsi:
                datprof_query = Datprof.objects.filter(provinsi=selected_provinsi)
            else:
                datprof_query = Datprof.objects.all()
        else:
            datprof_query = Datprof.objects.all()

        if selected_nama_data:
            datprof_query = datprof_query.filter(namadata__id=selected_nama_data)

        datprof_list = list(datprof_query.order_by('provinsi__name', 'tahun').values(
            'provinsi__id',
            'provinsi__name',
            'provinsi__latitude',
            'provinsi__longitude',
            'namadata__nama',
            'tahun',
            'jumlah'
        ))
    except (ValueError, TypeError):
        selected_provinsi = None
        datprof_list = []
    
    return render(request, 'kepadatan_penduduk.html', {
        'provinsi': provinsi,
        'provinsi_terpilih': provinsi_terpilih,
        'data_namadata': data_namadata,
        'selected_nama_data': selected_nama_data,
        'selected_nama_data_name': selected_nama_data_name,
        'selected_provinsi': selected_provinsi,
        'datprof_list_json': json.dumps(datprof_list, ensure_ascii=False),
        'datprof_list': datprof_list,
    })