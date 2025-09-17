# Data-Siswa
Data Siswa SMPN 21 Gunung Kidul (Data Dumy)
# Program Manajemen Data Siswa

Program ini dibuat untuk mengelola **data siswa** dengan fitur CRUD (Create, Read, Update, Delete) serta laporan sederhana.
Data siswa disimpan dalam bentuk **list of dictionary** di dalam kode.

# Fitur Utama

# Report Data

Menampilkan semua data siswa dalam bentuk tabel.

Menampilkan statistik nilai (rata-rata, nilai minimum, nilai maksimum).

Menampilkan ranking siswa berdasarkan rata-rata nilai.

# Tambah Data

Menambahkan data siswa baru dengan NIM unik.

# Ubah Data

Mengubah data siswa berdasarkan NIM.

# Hapus Data

Menghapus data siswa berdasarkan NIM.

# Cari Data

Mencari siswa berdasarkan NIM atau Nama.

# Keluar Program



# Struktur Data Siswa

Setiap siswa disimpan dalam bentuk dictionary:
{
  "NIM": "2200451",
  "Nama": "Lukman",
  "Praktek": 80,
  "Teori": 75,
  "Tugas": 80,
  "Kehadiran": 120,
  "Partisipasi": 89
}

# Cara Menjalankan Program

**1.** Pastikan Python sudah terinstall di komputer Anda.

**2.** Install library **tabulate** (untuk tampilan tabel):

pip install tabulate


**3.** Simpan kode program ke file, __**misalnya manajemen_siswa.py.**__

**4.** Jalankan program:

python manajemen_siswa.py


# Contoh Menu Utama
========= Menu Utama ========= 
1. Report Data  
2. Tambah Data
3. Ubah Data
4. Hapus Data
5. Cari Data
6. Keluar


# Statistik Nilai
Program akan menghitung:

 **- Rata-rata** setiap aspek penilaian

**- Nilai minimum** dan **maksimum**

=== Statistik Nilai ===
Praktek     : Rata-rata 74.00, Min 60, Max 90
Teori       : Rata-rata 85.80, Min 75, Max 99
Tugas       : Rata-rata 83.20, Min 79, Max 89
Kehadiran   : Rata-rata 115.20, Min 110, Max 120
Partisipasi : Rata-rata 86.60, Min 77, Max 99


# Catatan untuk Guru

**-** Program ini dirancang agar **mudah digunakan tanpa perlu pengetahuan teknis tinggi.**

**-** Input data cukup dengan mengetik angka atau teks sesuai petunjuk di layar.

**-** Hasil laporan ditampilkan otomatis dalam bentuk tabel agar mudah dibaca
