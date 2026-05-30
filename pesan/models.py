from django.db import models

class PesanAnonim(models.Model):
    isi_pesan = models.TextField()
    ip_pengirim = models.GenericIPAddressField(null=True, blank=True)
    perangkat_pengirim = models.CharField(max_length=255, null=True, blank=True)
    asal_link = models.CharField(max_length=100, default="Langsung/Ketik Sendiri")
    nama_pelacak = models.CharField(max_length=100, default="Anonim") # Untuk menangkap nama via parameter link
    waktu_dikirim = models.DateTimeField(auto_now_add=True)
    dibuka = models.BooleanField(default=False) # Untuk efek amplop terbuka/belum di inbox

    def __str__(self):
        return f"Pesan: {self.isi_pesan[:20]}... ({self.asal_link})"