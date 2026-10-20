
# GIS Analisis Lokasi Gerai

## Deskripsi
Proyek Sistem Informasi Geografis (GIS) untuk
menganalisis jarak antar-gerai dan menampilkan
lokasi gerai melalui peta interaktif.

Proyek ini dibuat sebagai studi kasus pembelajaran
GIS pada sektor ritel berdasarkan materi
Career and Competition in Industrial Era with GIS.

## Fitur
- Menampilkan lokasi gerai pada peta.
- Menghitung jarak antar-gerai.
- Mengidentifikasi pasangan gerai dengan jarak
  kurang dari 1 kilometer.
- Menyimpan hasil analisis ke file CSV.
- Menampilkan jangkauan simulasi pada peta.

## Teknologi
- Python
- Pandas
- Folium
- OpenStreetMap
- Git dan GitHub

## Cara Menjalankan
1. Instal library:
   pip install -r requirements.txt

2. Jalankan program:
   python main.py

3. Buka peta_gerai.html di browser.

## Struktur File
- main.py: kode utama program.
- gerai.csv: dataset koordinat gerai simulasi.
- requirements.txt: daftar library Python.
- hasil_analisis_jarak.csv: hasil analisis jarak.
- peta_gerai.html: peta interaktif.
