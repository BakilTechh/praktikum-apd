from time import sleep


# konfirmasi jika pilihan 0
def hitung_mundur(n):
    if n == 0:
        print("Berhasil\n")
        sleep(1)
    else:
        print(f"Bersiap dalam {n} detik...")
        sleep(1)
        hitung_mundur(n - 1)  # INI JUGA TERMASUK BAGIAN REKURSIFNYA

def konfirmasi_keluar():
    pilihan = input("Yakin ingin keluar? (y/Y untuk keluar): ")
    if pilihan.lower() == "y":
        hitung_mundur(3)  # Fungsi rekursifnya dipanggil di sini
        print("Baik, sampai jumpa. Kami tunggu diupdate hero selanjutnya.")
        return True
    else:
        print("Kembali ke menu.")
        return False