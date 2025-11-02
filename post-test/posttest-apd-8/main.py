import os
from time import sleep
from data import Orang, heroes  # data user dan hero
from hero import tampilkan_semua_hero,jumlah_hero,tampilkan_hero_berdasarkan_lane,cari_hero_berstatus,tambah_hero,ubah_hero,hapus_hero
from lainlain import hitung_mundur, konfirmasi_keluar

while True:  # LOOP LOGIN
    os.system('cls')
    print("=== Selamat datang di program Tier List hero Wajib Pick/Ban di Mobile Legends (PATCH OKTOBER AKHIR) ===")
    print("1. Login Admin")
    print("2. Login Member")
    print("3. Registrasi")
    print("0. Keluar dari program")
    pilihan_login = input("Masukkan pilihan: ")

    if pilihan_login == "0":
        if konfirmasi_keluar():
            break  # keluar dari program
        else:
            continue  # kembali ke menu login

    elif pilihan_login == "1" or pilihan_login == "2":
        username = input("Username: ")
        password = input("Password: ")

        if username in Orang and Orang[username]["password"] == password:
            if pilihan_login == "1" and Orang[username]["role"] == "admin":
                role = "admin"
            elif pilihan_login == "2" and Orang[username]["role"] == "member":
                role = "member"
            else:
                print("Role tidak sesuai.")
                sleep(2)
                continue  # kembali ke login

            # MASUK KE MENU UTAMA
            keluar = False
            os.system('cls')
            print("Selamat Datang yang mulia:", username, f"({role})", ", apa yang ingin anda lakukan?")
            sleep(2)
            while not keluar:
                print("=== MENU UTAMA ===")
                print("1. Lihat Hero")
                if role == "admin":
                    print("2. Tambah Hero")
                    print("3. Ubah Hero")
                    print("4. Hapus Hero")
                print("0. Kembali ke login")

                pilihan = input("Pilih menu: ")

                if pilihan == "0":
                    print("Kembali ke menu login...")
                    hitung_mundur(3)
                    keluar = True
                    sleep(1)
                    os.system('cls')

                elif pilihan == "1":
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
                        tampilkan_hero_berdasarkan_lane("Mid Lane")
                        sleep(1)
                        tampilkan_hero_berdasarkan_lane("Exp Lane")
                        sleep(1)
                        tampilkan_hero_berdasarkan_lane("Roaming")
                        sleep(1)
                        tampilkan_hero_berdasarkan_lane("Gold Lane")
                        sleep(1)
                        tampilkan_hero_berdasarkan_lane("Jungler")
                        sleep(1)
                        print("\n== BAGIAN STATUS DARI HERONYA ==")
                        cari_hero_berstatus("Auto ban")
                        sleep(1)
                        cari_hero_berstatus("Wajib pick")
                        sleep(1)
                        print("\nList ini adalah update patch terbaru dari hero-hero yang wajib pick/ban di Mobile Legends (PATCH OKTOBER AKHIR).")
                        print("Segera hubungi admin untuk menambahkan/merubah/menghapus hero selanjutnya.\n")
                    input("Tekan ENTER untuk kembali ke menu...")

                elif pilihan == "2" and role == "admin":
                    os.system('cls')
                    tambah_hero()
                    sleep(2)

                elif pilihan == "3" and role == "admin":
                    os.system('cls')
                    ubah_hero()
                    sleep(2)

                elif pilihan == "4" and role == "admin":
                    os.system('cls')
                    hapus_hero()
                    sleep(2)

                else:
                    print("Pilihan tidak valid.")
                    sleep(2)

        else:
            print("Username atau password salah.")
            sleep(2)

    elif pilihan_login == "3":
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