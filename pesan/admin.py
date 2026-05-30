from django.contrib import admin
from .models import PesanAnonim

@admin.register(PesanAnonim)
class PesanAnonimAdmin(admin.ModelAdmin):
    list_display = ('isi_pesan', 'asal_link', 'ip_pengirim', 'perangkat_pengirim', 'waktu_dikirim')