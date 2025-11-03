import os
from time import sleep
import inquirer  

from data import Orang, heroes
from hero import tampilkan_semua_hero, jumlah_hero, tampilkan_hero_berdasarkan_lane, cari_hero_berstatus, tambah_hero, ubah_hero, hapus_hero
from lainlain import hitung_mundur, konfirmasi_keluar

while True:  
    os.system('cls')
    print("=======================================================================================================")
    print("=== Selamat datang di program Tier List hero Wajib Pick/Ban di Mobile Legends (PATCH NOVEMBER AWAL) ===")
    print("=======================================================================================================\n")
    sleep(2)
    menu_login = [
        inquirer.List(
            "pilihan_login",
            message="Silakan pilih menu login sebagai? atau registrasi dulu?",
            choices=[
                "Admin",
                "Member",
                "Registrasi",
                "Keluar dari program"
            ]
        )
    ]
    jawaban = inquirer.prompt(menu_login)
    pilihan_login = jawaban["pilihan_login"]
    os.system('cls')
    print("====================================")
    print(f"Anda sudah memilih: {pilihan_login}")
    print("====================================\n")
    sleep(1)
    if pilihan_login == "Keluar dari program":
        if konfirmasi_keluar():
            break
        else:
            continue

    elif pilihan_login == "Admin" or pilihan_login == "Member":
        print(f"masukkan username dan passwordmu untuk login dulu\n")

        username = input("Username: ")
        password = input("Password: ")

        if username in Orang and Orang[username]["password"] == password:
            role = Orang[username]["role"]
            if pilihan_login == "Admin" and role != "admin":
                print("Role tidak sesuai.")
                sleep(2)
                continue
            elif pilihan_login == "Member" and role != "member":
                print("Role tidak sesuai.")
                sleep(2)
                continue

                # Masuk ke menu utama setelah login berhasil
            os.system('cls')
            print(f"Selamat Datang yang mulia: {username} ({role})")
            sleep(2)

            keluar = False
            while not keluar:
                menu_utama = ["Lihat Hero"]
                if role == "admin":
                    menu_utama += ["Tambah Hero", "Ubah Hero", "Hapus Hero"]
                menu_utama += ["Kembali ke login"]

                pilihan = inquirer.prompt([
                    inquirer.List("menu", message="Pilih menu utama", choices=menu_utama)
                ])["menu"]

                if pilihan == "Kembali ke login":
                    print("Kembali ke menu login...")
                    hitung_mundur(3)
                    keluar = True
                    sleep(1)
                    os.system('cls')

                elif pilihan == "Lihat Hero":
                    print("\nLIST HERO YANG META (PATCH OKTOBER):")
                    sleep(1)
                    if len(heroes) == 0:
                        print("Tidak ada hero yang overpowered.")
                    else:
                        tampilkan_semua_hero()
                        sleep(1)
                        jumlah_hero()
                        sleep(1)
                        print("\n== BAGIAN LANE DARI HERONYA ==")
                        for lane in ["Mid Lane", "Exp Lane", "Roaming", "Gold Lane", "Jungler"]:
                            tampilkan_hero_berdasarkan_lane(lane)
                            sleep(1)
                        print("\n== BAGIAN STATUS DARI HERONYA ==")
                        for status in ["Auto ban", "Wajib pick"]:
                            cari_hero_berstatus(status)
                            sleep(1)
                        print("\nList ini adalah update patch terbaru dari hero-hero yang wajib pick/ban di Mobile Legends (PATCH OKTOBER AKHIR).")
                        print("Segera hubungi admin untuk menambahkan/merubah/menghapus hero selanjutnya.\n")
                    input("Tekan ENTER untuk kembali ke menu...")

                elif pilihan == "Tambah Hero":
                    os.system('cls')
                    tambah_hero()
                    sleep(2)

                elif pilihan == "Ubah Hero":
                    os.system('cls')
                    ubah_hero()
                    sleep(2)

                elif pilihan == "Hapus Hero":
                    os.system('cls')
                    hapus_hero()
                    sleep(2)

        else:
            print("Username atau password salah.")
            sleep(2)

    elif pilihan_login == "Registrasi":
        print("\n=== Hai member baru, buat dulu username dan password mu ===")
        username_baru = input("Masukkan username baru: ")
        password_baru = input("Masukkan password baru: ")

        if username_baru in Orang:
            print("Username sudah dipakai. Silakan cari nama yg lain.\n")
            sleep(2)
        else:
            Orang[username_baru] = {"password": password_baru, "role": "member"}
            print("Registrasi berhasil. Silakan lanjut login sebagai member.\n")
            sleep(3)