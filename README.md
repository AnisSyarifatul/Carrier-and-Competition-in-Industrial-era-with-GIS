
# GIS Analisis Lokasi Gerai

## Studi Kasus

Proyek ini merupakan implementasi Geographic Information System (GIS) menggunakan Python untuk menganalisis persebaran lokasi gerai berdasarkan koordinat geografis. Program menghitung jarak antar-gerai, mengidentifikasi pasangan gerai yang berdekatan, menyimpan hasil analisis dalam file CSV, serta menampilkan lokasi gerai melalui peta interaktif.

Data koordinat yang digunakan merupakan data simulasi di sekitar Kota Bengkulu. Proyek ini bertujuan untuk memahami pemanfaatan teknologi GIS dalam analisis spasial, khususnya untuk membantu mengevaluasi kedekatan lokasi gerai sebagai salah satu pertimbangan dalam perencanaan usaha.

## Teknologi yang Digunakan

- **Python** — bahasa pemrograman utama.
- **Pandas** — membaca, mengolah, dan menyimpan data.
- **Folium** — membuat peta interaktif berbasis web.
- **OpenStreetMap** — menyediakan tampilan peta dasar.
- **Branca** — mendukung komponen visualisasi peta Folium.
- **Visual Studio Code** — lingkungan pengembangan program.
- **Git dan GitHub** — pengelolaan kode dan dokumentasi proyek.

## Fitur Program

### 1. Menampilkan Data Gerai

Program membaca dataset `gerai.csv` dan menampilkan nama gerai beserta koordinat latitude dan longitude.

### 2. Menghitung Jarak Antar-Gerai

Program menghitung jarak setiap pasangan gerai menggunakan rumus Haversine. Metode ini memperkirakan jarak terpendek antara dua titik pada permukaan bumi berdasarkan koordinat geografis.

### 3. Mengidentifikasi Gerai yang Berdekatan

Program menggunakan ambang jarak simulasi sebesar 1 kilometer untuk mengelompokkan pasangan gerai menjadi:

- **Berdekatan**: jarak antar-gerai kurang dari 1 kilometer.
- **Tidak berdekatan**: jarak antar-gerai sama dengan atau lebih dari 1 kilometer.

Ambang tersebut digunakan untuk demonstrasi analisis dan bukan standar resmi dalam penentuan lokasi usaha.

### 4. Menyimpan Hasil Analisis

Hasil perhitungan jarak seluruh pasangan gerai disimpan secara otomatis ke dalam file `hasil_analisis_jarak.csv`.

Informasi yang disimpan meliputi nama kedua gerai, jarak dalam kilometer, dan status kedekatan.

### 5. Membuat Peta Interaktif

Program menghasilkan peta interaktif dalam file `peta_gerai.html`. Setiap gerai ditampilkan menggunakan penanda lokasi yang dapat diklik untuk melihat informasi koordinatnya.

Peta juga menampilkan lingkaran dengan radius 1 kilometer di sekitar setiap gerai sebagai visualisasi jangkauan simulasi.

## Algoritma dan Metode

### Rumus Haversine

Rumus Haversine digunakan untuk menghitung jarak geografis antara dua titik berdasarkan latitude dan longitude.

Proses perhitungan melibatkan konversi koordinat ke radian, perhitungan selisih koordinat, dan penggunaan trigonometri untuk memperoleh jarak dalam kilometer.

Program menggunakan perkiraan radius bumi sebesar 6.371 kilometer.

### Kombinasi Pasangan Gerai

Program menggunakan fungsi `combinations()` dari modul `itertools` untuk menghasilkan seluruh pasangan gerai yang berbeda tanpa mengulang pasangan yang sama.

Dengan lima gerai, program menghitung jarak sebanyak 10 pasangan.

## Dataset

Dataset disimpan dalam file `gerai.csv` dengan tiga atribut utama.

| Atribut | Keterangan |
|---|---|
| `nama_gerai` | Nama atau identitas gerai. |
| `latitude` | Koordinat garis lintang lokasi gerai. |
| `longitude` | Koordinat garis bujur lokasi gerai. |

### Contoh Dataset

```csv id="3vl1l2"
nama_gerai,latitude,longitude
Gerai A,-3.8005,102.2655
Gerai B,-3.8060,102.2720
Gerai C,-3.7900,102.2800
Gerai D,-3.8150,102.2600
Gerai E,-3.7980,102.2500
```

**Catatan:** Seluruh koordinat merupakan data simulasi di sekitar Kota Bengkulu, bukan hasil survei lokasi usaha yang telah diverifikasi.

## Alur Kerja Program

1. Membaca dataset koordinat dari `gerai.csv`.
2. Menampilkan jumlah dan informasi lokasi gerai.
3. Membentuk seluruh pasangan gerai yang berbeda.
4. Menghitung jarak setiap pasangan menggunakan rumus Haversine.
5. Menentukan status kedekatan berdasarkan ambang 1 kilometer.
6. Menyimpan hasil analisis ke `hasil_analisis_jarak.csv`.
7. Membuat peta interaktif menggunakan Folium.
8. Menambahkan penanda gerai dan lingkaran jangkauan simulasi.
9. Menyimpan peta ke `peta_gerai.html` agar dapat dibuka melalui browser.

## Struktur Folder

```text id="y4j2of"
gis-analisis-gerai/
├── main.py
├── gerai.csv
├── requirements.txt
├── hasil_analisis_jarak.csv
├── peta_gerai.html
└── README.md
```

Keterangan:

- `main.py`: kode utama untuk menghitung jarak dan membuat peta.
- `gerai.csv`: dataset koordinat gerai.
- `requirements.txt`: daftar dependensi Python.
- `hasil_analisis_jarak.csv`: hasil perhitungan jarak antar-gerai yang dibuat oleh program.
- `peta_gerai.html`: peta interaktif yang dibuat oleh program.
- `README.md`: dokumentasi proyek.

File `hasil_analisis_jarak.csv` dan `peta_gerai.html` akan dibuat setelah program berhasil dijalankan.

## Output Program

Program menghasilkan tiga jenis keluaran utama:

1. **Terminal:** menampilkan jumlah gerai, daftar koordinat, jarak setiap pasangan gerai, dan status kedekatannya.
2. **`hasil_analisis_jarak.csv`:** menyimpan tabel hasil perhitungan jarak antar-gerai.
3. **`peta_gerai.html`:** menampilkan peta interaktif dengan penanda lokasi dan lingkaran jangkauan simulasi.

Jumlah pasangan yang dianalisis untuk lima gerai adalah:

```text id="h7d2kv"
Jumlah gerai: 5
Jumlah pasangan yang dianalisis: 10
Ambang jarak simulasi: 1.0 km
```

## Manfaat Proyek

- Membantu memahami analisis spasial berbasis koordinat geografis.
- Mempermudah visualisasi persebaran lokasi gerai.
- Menyediakan informasi jarak antar-gerai secara otomatis.
- Menghasilkan laporan yang dapat dibuka menggunakan aplikasi spreadsheet.
- Menjadi dasar pengembangan sistem pendukung keputusan lokasi usaha.

## Kesimpulan

Proyek ini menerapkan Geographic Information System (GIS) menggunakan Python untuk menganalisis jarak dan persebaran lokasi gerai. Dengan rumus Haversine, program menghitung jarak setiap pasangan gerai dan mengidentifikasi kedekatannya berdasarkan ambang simulasi 1 kilometer.

Hasil analisis disimpan dalam file CSV, sedangkan persebaran lokasi ditampilkan melalui peta interaktif menggunakan Folium. Proyek ini menjadi dasar pembelajaran analisis spasial yang dapat dikembangkan untuk mendukung perencanaan lokasi usaha berbasis data.