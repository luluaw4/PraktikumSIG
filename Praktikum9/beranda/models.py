from django.db import models

#create your models here.
class Provinsi(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)  # VARCHAR di Django memerlukan max_length
    alt_name = models.CharField(max_length=255, default='', blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'provinces'  # Menyesuaikan dengan nama tabel di database asli

    def __str__(self):
        return self.name

class Kabkota(models.Model):
    id = models.BigIntegerField(primary_key=True)
    province = models.ForeignKey(
        Provinsi, 
        on_delete=models.CASCADE, 
        db_column='province_id',  # Menyesuaikan nama kolom foreign key di tabel asli
        related_name='kabkota_set'
    )
    name = models.CharField(max_length=255)  # VARCHAR memerlukan max_length di Django
    alt_name = models.CharField(max_length=255, default='', blank=True)
    latitude = models.FloatField(default=0.0)   # DOUBLE PRECISION dipetakan ke FloatField
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'regencies'  # Menyesuaikan nama tabel di database asli

    def __str__(self):
        return self.name
    
class Kecamatan(models.Model):
    id = models.BigIntegerField(primary_key=True)
    regency = models.ForeignKey(
        Kabkota, 
        on_delete=models.CASCADE, 
        db_column='regency_id',  # Menyesuaikan nama kolom foreign key di database asli
        related_name='kecamatan_set'
    )
    name = models.CharField(max_length=255)  # VARCHAR memerlukan max_length di Django
    alt_name = models.CharField(max_length=255, default='', blank=True)
    latitude = models.FloatField(default=0.0)   # DOUBLE PRECISION dipetakan ke FloatField
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'districts'  # Menyesuaikan dengan nama tabel asli di SQL

    def __str__(self):
        return self.name

class Kelurahan(models.Model):
    id = models.BigIntegerField(primary_key=True)
    district = models.ForeignKey(
        Kecamatan, 
        on_delete=models.CASCADE, 
        db_column='district_id',  # Menyesuaikan nama kolom foreign key di database asli
        related_name='kelurahan_set'
    )
    name = models.CharField(max_length=255)  # VARCHAR memerlukan max_length di Django
    alt_name = models.CharField(max_length=255, default='', blank=True)
    latitude = models.FloatField(default=0.0)   # DOUBLE PRECISION dipetakan ke FloatField
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'villages'  # Menyesuaikan nama tabel asli di database SQL

    def __str__(self):
        return self.name
    
class NamaData(models.Model):
    nama = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'nama_data'

    def __str__(self):
        return self.nama


class Datprof(models.Model):
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
    namadata = models.ForeignKey(NamaData, on_delete=models.CASCADE)
    tahun = models.IntegerField()
    jumlah = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'datprof'
        unique_together = ('provinsi', 'namadata', 'tahun')

    def __str__(self):
        return f"{self.provinsi.name} - {self.namadata.nama} - {self.tahun}"