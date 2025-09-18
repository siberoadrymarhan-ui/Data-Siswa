import statistics
from tabulate import tabulate

# ===================== Data Awal =====================
data_siswa = [
    {"NIM": "2200451", "Nama": "Lukman",  "Praktek": 80, "Teori": 75, "Tugas": 80, "Kehadiran": 120, "Partisipasi": 89},
    {"NIM": "2200452", "Nama": "Ayu",     "Praktek": 90, "Teori": 78, "Tugas": 89, "Kehadiran": 111, "Partisipasi": 78},
    {"NIM": "2200453", "Nama": "Bayu",    "Praktek": 60, "Teori": 88, "Tugas": 80, "Kehadiran": 120, "Partisipasi": 77},
    {"NIM": "2200454", "Nama": "Michael", "Praktek": 75, "Teori": 99, "Tugas": 88, "Kehadiran": 110, "Partisipasi": 90},
    {"NIM": "2200455", "Nama": "Cindy",   "Praktek": 65, "Teori": 89, "Tugas": 79, "Kehadiran": 115, "Partisipasi": 99},
]

# ===================== Fungsi Utility =====================
def hitung_rata(d):
    return (d['Praktek'] + d['Teori'] + d['Tugas'] + d['Kehadiran'] + d['Partisipasi']) / 5

def tampilkan_data(dataset):
    """Tampilkan data siswa dalam bentuk tabel"""
    if not dataset:
        print("\n[!] Data kosong.\n")
        return
    tabel = []
    for i, d in enumerate(dataset, start=1):
        tabel.append([
            i, d["NIM"], d["Nama"], d["Praktek"], d["Teori"], d["Tugas"],
            d["Kehadiran"], d["Partisipasi"], f"{hitung_rata(d):.2f}"
        ])
    headers = ["No", "NIM", "Nama", "Praktek", "Teori", "Tugas", "Hadir", "Part", "Rata2"]
    print(tabulate(tabel, headers=headers, tablefmt="grid"))

# ===================== CRUD & REPORT =====================
def report_data():
    while True:
        print("""
--- Report Data ---
1. Tampilkan Semua Data
2. Statistik Nilai
3. Ranking Siswa
4. Kembali
""")
        pilih = input("Pilih [1-4]: ")
        if pilih == "1":
            tampilkan_data(data_siswa)
        elif pilih == "2":
            print("\n=== Statistik Nilai ===")
            for k in ["Praktek", "Teori", "Tugas", "Kehadiran", "Partisipasi"]:
                nilai = [d[k] for d in data_siswa]
                print(f"{k:<12}: Rata-rata {statistics.mean(nilai):.2f}, Min {min(nilai)}, Max {max(nilai)}")
        elif pilih == "3":
            ranking = sorted(data_siswa, key=lambda x: hitung_rata(x), reverse=True)
            print("\n=== Ranking Siswa ===")
            tampilkan_data(ranking)
        elif pilih == "4":
            break

def tambah_data():
    nim = input("NIM: ")
    if any(d["NIM"] == nim for d in data_siswa):
        print("[!] NIM sudah ada.")
        return
    nama = input("Nama: ")
    praktek = int(input("Nilai Praktek: "))
    teori = int(input("Nilai Teori: "))
    tugas = int(input("Nilai Tugas: "))
    hadir = int(input("Kehadiran: "))
    part = int(input("Partisipasi: "))
    data_baru = {"NIM": nim, "Nama": nama, "Praktek": praktek,
                 "Teori": teori, "Tugas": tugas, "Kehadiran": hadir,
                 "Partisipasi": part}
    data_siswa.append(data_baru)
    print("[✓] Data berhasil ditambahkan.")

def ubah_data():
    nim = input("Masukkan NIM yang akan diubah: ")
    for d in data_siswa:
        if d["NIM"] == nim:
            print("Data ditemukan, isi baru (biarkan kosong jika tidak diubah):")
            for key in ["Nama", "Praktek", "Teori", "Tugas", "Kehadiran", "Partisipasi"]:
                baru = input(f"{key} ({d[key]}): ")
                if baru:
                    d[key] = int(baru) if key != "Nama" else baru
            print("[✓] Data berhasil diubah.")
            return
    print("[!] Data tidak ditemukan.")

def hapus_data():
    nim = input("Masukkan NIM yang akan dihapus: ")
    for i, d in enumerate(data_siswa):
        if d["NIM"] == nim:
            del data_siswa[i]
            print("[✓] Data berhasil dihapus.")
            return
    print("[!] Data tidak ditemukan.")

def cari_data():
    key = input("Masukkan NIM/Nama: ").lower()
    hasil = [d for d in data_siswa if key in d["NIM"].lower() or key in d["Nama"].lower()]
    tampilkan_data(hasil)

# ===================== Menu Utama =====================
def menu_utama():
    while True:
        print("""
========= Menu Utama ========= 
1. Report Data  
2. Tambah Data
3. Ubah Data
4. Hapus Data
5. Cari Data
6. Keluar
""")
        pilih = input("Pilih [1-6]: ")
        if pilih == "1": report_data()
        elif pilih == "2": tambah_data()
        elif pilih == "3": ubah_data()
        elif pilih == "4": hapus_data()
        elif pilih == "5": cari_data()
        elif pilih == "6":
            print("Terima kasih, program selesai.")
            break
        else:
            print("[!] Pilihan salah.")

# ===================== Jalankan Program =====================
menu_utama()
