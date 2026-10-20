
# GIS Analisis Lokasi Gerai

## STUDI KASUS
Pemanfaatan Geographic Information System (GIS) di sektor ritel dapat membantu menganalisis persebaran dan jarak antar-gerai sebagai bahan pertimbangan dalam menentukan lokasi usaha. Proyek ini mengembangkan program berbasis Python untuk menampilkan lokasi gerai pada peta interaktif, menghitung jarak antar-gerai, serta mengidentifikasi gerai yang berdekatan berdasarkan ambang jarak simulasi 1 kilometer. Data koordinat yang digunakan merupakan data simulasi di sekitar Kota Bengkulu, sehingga hasil analisis hanya digunakan untuk demonstrasi dan belum menjadi rekomendasi lokasi bisnis yang sebenarnya.

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
