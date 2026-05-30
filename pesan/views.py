from django.shortcuts import render, get_object_or_404
from .models import PesanAnonim

def dapatkan_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# 1. Halaman utama tempat orang kirim pesan anonim
def kirim_pesan_view(request):
    status_sukses = False
    # Ambil parameter nama dari link jika ada (misal: ?nama=Wahyu)
    nama_terdeteksi = request.GET.get('nama', 'Anonim')
    
    if request.method == 'POST':
        isi = request.POST.get('isi_pesan')
        if isi:
            ip = dapatkan_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', 'Tidak Diketahui')
            
            # Deteksi asal link otomatis
            referer = request.META.get('HTTP_REFERER', '').lower()
            sumber = 'Klik Langsung / Salin Tautan'
            
            if 'instagram.com' in referer:
                sumber = 'Instagram (Story/Bio)'
            elif 'whatsapp.com' in referer or 'wa.me' in referer:
                sumber = 'WhatsApp (Chat/Status)'
            elif 'tiktok.com' in referer:
                sumber = 'TikTok'
            
            # Jika di link ada manual param ?sumber=ig
            param_sumber = request.GET.get('sumber')
            if param_sumber:
                sumber = param_sumber.upper()

            PesanAnonim.objects.create(
                isi_pesan=isi,
                ip_pengirim=ip,
                perangkat_pengirim=user_agent,
                asal_link=sumber,
                nama_pelacak=nama_terdeteksi
            )
            status_sukses = True
            
    return render(request, 'pesan/index.html', {'sukses': status_sukses})

# 2. Halaman Kotak Masuk (Inbox Berupa Amplop)
def inbox_view(request):
    semua_pesan = PesanAnonim.objects.all().order_by('-waktu_dikirim')
    return render(request, 'pesan/inbox.html', {'semua_pesan': semua_pesan})

# 3. Halaman Detail Pesan (Melihat isi pesan + Deteksi Rahasia)
def detail_pesan_view(request, pk):
    pesan = get_object_or_404(PesanAnonim, pk=pk)
    pesan.dibuka = True
    pesan.save()
    return render(request, 'pesan/detail.html', {'pesan': pesan})