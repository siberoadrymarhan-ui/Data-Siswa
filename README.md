# Program Manajemen Data Siswa
Data Siswa SMPN 21 Gunung Kidul (Data Dumy)

Program ini dibuat untuk mengelola **data siswa** dengan fitur CRUD (Create, Read, Update, Delete) serta laporan sederhana.
Data siswa disimpan dalam bentuk **list of dictionary** di dalam kode.

# Deskripsi Program
Program ini dirancang untuk membantu guru dalam mengelola data siswa dengan mudah.
Fungsi utama yang bisa dilakukan:

**-** Menambahkan data siswa baru

**-** Mengubah data siswa yang sudah ada

**-** Menghapus data siswa

**-** Mencari data siswa berdasarkan NIM atau Nama

**-** Menampilkan laporan (data lengkap, statistik nilai, dan ranking siswa)

Data disajikan dalam bentuk tabel rapi menggunakan library tabulate sehingga mudah dibaca.

# User
Guru mata pelajaran atau wali kelas murid sebagai pengguna utama aplikasi

# Keterbatasan
1. data bersifat sementara, yang dimana apabila program ataupun sistem di hapus, data akan terhapus otomatis
2. bisa disimpan datanya dengan menyimpan daata ke file seperti CSV, JSON, dll.


# Data yang Dicatat

Setiap siswa memiliki informasi:

**-** NIM (Nomor Induk Mahasiswa)

**-** Nama

**-** Nilai Praktek

**-** Nilai Teori

**-** Nilai Tugas

**-** Kehadiran

**-** Partisipasi


# Panduan Penggunaan untuk Guru

**1. Panduan Penggunaan untuk Guru**
Saat program dijalankan, akan muncul:

========= Menu Utama ========= 

Total data siswa: 5

1. Report Data  
2. Tambah Data
3. Ubah Data
4. Hapus Data
5. Cari Data
6. Keluar


➡ Guru bisa memilih angka **1 sampai 6** sesuai kebutuhan.

**2. Report Data (_Laporan_)**

Pilihan ini digunakan untuk melihat laporan nilai siswa.

--- Report Data ---
1. Tampilkan Semua Data
2. Statistik Nilai
3. Ranking Siswa
4. Kembali


**-** **Tampilkan Semua Data** → Menampilkan seluruh data siswa dalam tabel.

**-** **Statistik Nilai** → Menampilkan rata-rata, nilai tertinggi, dan terendah dari tiap kategori (Praktek, Teori, Tugas, Kehadiran, Partisipasi).

**-** **Ranking Siswa** → Menampilkan urutan siswa berdasarkan nilai rata-rata (dari tertinggi ke terendah).

**-** **Kembali** → Kembali ke menu utama.


**3. Tambah Data**

Guru bisa memasukkan data siswa baru dengan mengetik NIM, Nama, dan nilai.

Contoh:
[
NIM: 2200456

Nama: bayu

Nilai Praktek: 85

Nilai Teori: 88

Nilai Tugas: 92

Kehadiran: 119

Partisipasi: 95

[✓] Data berhasil ditambahkan

Total siswa sekarang: 6
]

**4. Ubah Data**

Guru bisa memperbarui data siswa jika ada kesalahan atau perubahan.

Masukkan NIM yang akan diubah: 2200452
Data ditemukan, isi baru (biarkan kosong jika tidak diubah):
Nama (Ayu): Ayu Lestari
Praktek (90):
Teori (78): 82
Tugas (89):
Kehadiran (111):
Partisipasi (78): 80
[✓] Data berhasil diubah.


➡ Jika guru tidak ingin mengubah salah satu nilai, cukup tekan **Enter.**

**5. Hapus Data**

Menghapus data siswa yang sudah tidak diperlukan.

Masukkan NIM yang akan dihapus: 2200453
[✓] Data berhasil dihapus.
Total siswa sekarang: 5

**6. Cari Data**

Guru bisa mencari siswa berdasarkan **NIM atau Nama.**

Masukkan NIM/Nama: ayu
+----+----------+-------------+-----------+---------+---------+---------+---------+---------+
| No | NIM      | Nama        |   Praktek |   Teori |   Tugas |   Hadir |   Part  |   Rata2 |
+====+==========+=============+===========+=========+=========+=========+=========+=========+
|  1 | 2200452  | Ayu Lestari |        90 |      82 |      89 |     111 |      80 |   90.40 |
+----+----------+-------------+-----------+---------+---------+---------+---------+---------+
Jumlah hasil pencarian: 1 siswa

**7. Keluar**

Jika sudah selesai, pilih menu 6 untuk keluar:

Terima kasih, program selesai.


# Manfaat untuk Guru


**1.** Tidak perlu menghitung manual rata-rata dan ranking siswa.

**2.** Mudah melacak nilai tertinggi, terendah, dan rata-rata.

**3.** Bisa mencari siswa tertentu dengan cepat.

**4.** Menambahkan dan memperbarui data lebih rapi dan cepat.

**5.** Semua data tampil dalam tabel sehingga mudah dibaca saat evaluasi.

# Cara Menjalankan Program

1. Pastikan Python sudah terpasang di komputer.

2. Install library tabulate (jika belum ada):

    pip install tabulate

3. Simpan kode Python dengan nama _data_siswa.py._

4. Jalankan program dengan perintah:

    python data_siswa.py
