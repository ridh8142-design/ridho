# TUGAS MODUL 3 - PSEUDOCODE
# Mata Kuliah : Pemrograman Dasar & Struktur Data
# Nama        : Muhammad Ridho Audri
# NIM         : 412610172
# Dosen       : Anjeng Puspita Ningrum, S.Kom.
#
# Program dibuat berdasarkan 4 latihan pada Modul 3.

def soal_1_minimarket():
    print("\n=== SOAL 1: DISKON MINIMARKET ===")
    total_belanja = float(input("Masukkan total belanja (Rp): "))

    if total_belanja < 0:
        print("Total belanja tidak boleh negatif.")
        return

    if total_belanja >= 100000:
        diskon = total_belanja * 0.10
    else:
        diskon = 0

    total_bayar = total_belanja - diskon
    print(f"Total belanja : Rp{total_belanja:,.2f}")
    print(f"Diskon        : Rp{diskon:,.2f}")
    print(f"Total bayar   : Rp{total_bayar:,.2f}")


def soal_2_kelulusan():
    print("\n=== SOAL 2: PENENTUAN KELULUSAN ===")
    nilai = float(input("Masukkan nilai akhir mahasiswa: "))

    if nilai > 60:
        print("Status: LULUS")
    else:
        print("Status: TIDAK LULUS")


def soal_3_tahun_kabisat():
    print("\n=== SOAL 3: TAHUN KABISAT ===")
    tahun = int(input("Masukkan tahun: "))

    if tahun <= 0:
        print("Tahun harus berupa bilangan positif.")
        return

    if tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0):
        print(f"Tahun {tahun} adalah tahun kabisat.")
    else:
        print(f"Tahun {tahun} bukan tahun kabisat.")


def soal_4_konversi_suhu():
    print("\n=== SOAL 4: KONVERSI SUHU ===")
    celsius = float(input("Masukkan suhu dalam Celsius: "))

    reamur = 4 / 5 * celsius
    fahrenheit = 9 / 5 * celsius + 32

    print(f"Celsius   : {celsius:.2f} °C")
    print(f"Reamur    : {reamur:.2f} °R")
    print(f"Fahrenheit: {fahrenheit:.2f} °F")


def main():
    while True:
        print("\n==========================================")
        print(" TUGAS MODUL 3 - PEMROGRAMAN DASAR")
        print(" Muhammad Ridho Audri | 412610172")
        print("==========================================")
        print("1. Menghitung diskon minimarket")
        print("2. Menentukan kelulusan mahasiswa")
        print("3. Menentukan tahun kabisat")
        print("4. Konversi Celsius ke Reamur dan Fahrenheit")
        print("0. Keluar")

        pilihan = input("Pilih program (0-4): ")

        if pilihan == "1":
            soal_1_minimarket()
        elif pilihan == "2":
            soal_2_kelulusan()
        elif pilihan == "3":
            soal_3_tahun_kabisat()
        elif pilihan == "4":
            soal_4_konversi_suhu()
        elif pilihan == "0":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 0 sampai 4.")


if __name__ == "__main__":
    main()
