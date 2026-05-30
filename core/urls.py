from django.contrib import admin
from django.urls import path
from pesan.views import kirim_pesan_view, inbox_view, detail_pesan_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', kirim_pesan_view, name='kirim_pesan'),
    path('inbox/', inbox_view, name='inbox_pesan'),
    path('pesan/<int:pk>/', detail_pesan_view, name='detail_pesan'),
]