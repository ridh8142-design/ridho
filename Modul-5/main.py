# TUGAS MODUL 5 - TIPE DATA
# Mata Kuliah : Lab Pemrograman Dasar dan Struktur Data
# Nama        : Muhammad Ridho Audri
# NIM         : 412610172
# Dosen       : Anjeng Puspita Ningrum, S.Kom

print("=" * 55)
print("TUGAS MODUL 5 - TIPE DATA")
print("Muhammad Ridho Audri | 412610172")
print("=" * 55)

# 1. Mengolah string: mengganti kata dan mengubah huruf menjadi kapital
print("\n1. PENGGUNAAN STRING")
kalimat = "belajar coding sangat menyenangkan"
print("Kalimat awal       :", kalimat)

kalimat = kalimat.replace("menyenangkan", "keren")
print("Setelah replace    :", kalimat)

kalimat = kalimat.upper()
print("Setelah uppercase  :", kalimat)

# 2. Membuat variabel dengan tipe data berbeda dan menampilkan tipenya
print("\n2. JENIS-JENIS TIPE DATA")
a = 100
b = 3.14
c = "halo semuanya"

print("Nilai a :", a, "| Tipe data:", type(a).__name__)
print("Nilai b :", b, "| Tipe data:", type(b).__name__)
print("Nilai c :", c, "| Tipe data:", type(c).__name__)

# 3. Membuat list warna dan mengubah elemen ketiga
print("\n3. PENGGUNAAN LIST")
warna = ["merah", "biru", "hijau", "kuning", "ungu"]
print("List warna sebelum diubah :", warna)

warna[2] = "jingga"
print("List warna setelah diubah :", warna)
print("Elemen ketiga sekarang    :", warna[2])

print("\n" + "=" * 55)
print("SELURUH TUGAS MODUL 5 SELESAI DIJALANKAN")
print("=" * 55)
