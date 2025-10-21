# POSTTEST 6
# MUHAMMAD BAKIL AMRU 
# 2509106044
# SET AND DICTIONARY 
import os
from time import sleep
os.system('cls')


Orang = {
    "bakil": {"password": "admin#1234", "role": "admin"},
    "member": {"password": "member#1234", "role": "member"}
}

heroes = {
    1: {"nama": "Angela", "lane": "Mid Lane", "role": "Support", "status": "Auto ban"},
    2: {"nama": "Yi-Shun-shin", "lane": "Jungler", "role": "Assasin", "status": "Auto ban"},
    3: {"nama": "Diggie", "lane": "Roaming", "role": "Support", "status": "Wajib pick"},
    4: {"nama": "Natan", "lane": "Gold Lane", "role": "Marksman", "status": "Auto ban"},
    5: {"nama": "Bane", "lane": "Exp Lane", "role": "Fighter", "status": "Broken"}
}

lanes = ["Jungler", "Roaming", "Exp", "Gold", "Mid"]
roles_hero = ["Tank", "Fighter", "Assasin", "Marksman", "Mage", "Support"]
status_hero = ["Auto ban", "Wajib pick", "Broken", "Meta", "Situasional"]


role = None
username = None

# MASUK KE BAGIAN REGISTRASI
while True:
    os.system('cls')
    print("=== Selamat datang di program Tier list Hero Wajib pick/ban untuk hero Mobile Legends ===")
    print("Siapa yang ingin login?")
    print("1. Admin")
    print("2. Member")
    print("3. Mendaftar sebagai member")
    pilihan_login = input("Masukkan pilihan (1/2/3): ")

    if pilihan_login not in ["1", "2", "3"]:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.\n")
        continue

    if pilihan_login in ["1", "2"]:
        username = input("Username: ")
        password = input("Password: ")

        if username in Orang and Orang[username]["password"] == password:
            if pilihan_login == "1" and Orang[username]["role"] == "admin":
                role = "admin"
                break
            elif pilihan_login == "2" and Orang[username]["role"] == "member":
                role = "member"
                break
            else:
                print("Role tidak sesuai.\n")
                sleep(2)
        else:
            print("Username atau password salah.\n")
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
            print("Registrasi berhasil Silakan lanjut login sebagai member.\n")
            sleep(3)

if role:
    os.system('cls')
    print("Selamat Datang yang mulia", username, f"({role})", "apa yang ingin anda lakukan?")
    keluar = False

    while not keluar:
        print("\n=== MENU ===")
        print("1. Melihat Tier list Hero")
        if role == "admin":
            print("2. Menambahkan Hero")
            print("3. Mengubah Hero")
            print("4. Menghapus Hero")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        # 1. Melihat Tier List
        if pilihan == "1":
            os.system('cls')
            print("\nLIST HERO YANG META (PATCH OKTOBER):")
            if len(heroes) == 0:
                print("Tidak ada hero yang overpowered.")
            else:
                print("=" * 70)
                print(f"{'No':<3} {'Hero':<15} {'Lane':<15} {'Role':<12} {'Status':<20}")
                print("=" * 70)
                for nomor_hero, hero in heroes.items():
                    print(f"{nomor_hero:<3} {hero['nama']:<15} {hero['lane']:<15} {hero['role']:<12} {hero['status']:<20}")

        # 2. Menambahkan Hero
        elif pilihan == "2" and role == "admin":
            nama = input("Nama Hero: ")
            ada_angka = False
            for karakter in nama:
                if karakter in "0123456789":
                    ada_angka = True
                    break

            if ada_angka:
                print("Nama hero tidak boleh mengandung angka.")
            else:
                print("\nPilih Lane:")
                print("1. Mid Lane\n2. Jungler\n3. Roaming\n4. Gold Lane\n5. Exp Lane")
                lane_input = input("Masukkan nomor lane (1-5): ")
                lane = None
                if lane_input in ["1", "2", "3", "4", "5"]:
                    lane = lanes[int(lane_input)-1] + " Lane"
                else:
                    print("Pilihan lane tidak valid.")
                    lane = None

                if lane:
                    print("\nPilih Role:")
                    print("1. Tank\n2. Fighter\n3. Assasin\n4. Marksman\n5. Mage\n6. Support")
                    role_input = input("Masukkan nomor role: ")
                    role_hero = None
                    if role_input in ["1", "2", "3", "4", "5", "6"]:
                        role_hero = roles_hero[int(role_input)-1]
                    else:
                        print("Pilihan role tidak valid.")
                        role_hero = None

                    if role_hero:
                        print("\nPilih Status:")
                        print("1. Auto ban\n2. Wajib pick\n3. Broken\n4. Meta\n5. Situasional")
                        status_input = input("Masukkan nomor status: ")
                        status = None
                        if status_input in ["1", "2", "3", "4", "5"]:
                            status = status_hero[int(status_input)-1]
                        else:
                            print("Pilihan status tidak valid.")
                            status = None

                        if status:
                            nomor_tertinggi = 0
                            for nomor in heroes:
                                if nomor > nomor_tertinggi:
                                    nomor_tertinggi = nomor
                            nomor_baru = nomor_tertinggi + 1

                            heroes[nomor_baru] = {
                                "nama": nama,
                                "lane": lane,
                                "role": role_hero,
                                "status": status
                            }
                            os.system('cls')
                            print("Hero berhasil ditambahkan.")
                            sleep (2)

        # 3. Mengubah Hero
        elif pilihan == "3" and role == "admin":
            os.system('cls')
            if len(heroes) == 0:
                print("Belum ada hero untuk diubah.")
            else:
                print("\nDAFTAR HERO:")
                print("=" * 70)
                print(f"{'No':<3} {'Hero':<15} {'Lane':<15} {'Role':<12} {'Status':<20}")
                print("=" * 70)
                for nomor_hero, hero in heroes.items():
                    print(f"{nomor_hero:<3} {hero['nama']:<15} {hero['lane']:<15} {hero['role']:<12} {hero['status']:<20}")

                ubah_input = input("Pilih nomor hero yang ingin kamu ubah: ")
                if ubah_input in [str(n) for n in heroes]:
                    ubah = int(ubah_input)
                    nama = input("Nama Heronya: ")
                    ada_angka = False
                    for karakter in nama:
                        if karakter in "0123456789":
                            ada_angka = True
                            break

                    if ada_angka:
                        print("Nama hero tidak boleh mengandung angka.")
                    else:
                        print("\nPilih Lane:")
                        print("1. Mid Lane\n2. Jungler\n3. Roaming\n4. Gold Lane\n5. Exp Lane")
                        lane_input = input("Masukkan nomor lane (1-5): ")
                        lane = None
                        if lane_input in ["1", "2", "3", "4", "5"]:
                            lane = lanes[int(lane_input)-1] + " Lane"
                        else:
                            print("Pilihan lane tidak valid.")
                            lane = None

                        if lane:
                            print("\nPilih Role:")
                            print("1. Tank\n2. Fighter\n3. Assasin\n4. Marksman\n5. Mage\n6. Support")
                            role_input = input("Masukkan nomor role: ")
                            role_hero = None
                            if role_input in ["1", "2", "3", "4", "5", "6"]:
                                role_hero = roles_hero[int(role_input)-1]
                            else:
                                print("Pilihan role tidak valid.")
                                role_hero = None

                            if role_hero:
                                print("\nPilih Status:")
                                print("1. Auto ban\n2. Wajib pick\n3. Broken\n4. Meta\n5. Situasional")
                                status_input = input("Masukkan nomor status: ")
                                status = None
                                if status_input in ["1", "2", "3", "4", "5"]:
                                    status = status_hero[int(status_input)-1]
                                else:
                                    print("Pilihan status tidak valid.")
                                    status = None

                                if status:
                                    heroes[ubah] = {
                                        "nama": nama,
                                        "lane": lane,
                                        "role": role_hero,
                                        "status": status
                                    }
                                    os.system('cls')
                                    print("Hero berhasil diubah.")
                                    sleep(2)
                else:
                    print("Nomor tidak valid.")

        # 4. Menghapus Hero
        elif pilihan == "4" and role == "admin":
            os.system('cls')
            if len(heroes) == 0:
                print("Belum ada hero untuk dihapus.")
            else:
                print("\nDAFTAR HERO:")
                print("=" * 70)
                print(f"{'No':<3} {'Hero':<15} {'Lane':<15} {'Role':<12} {'Status':<20}")
                print("=" * 70)
                for nomor_hero, hero in heroes.items():
                    print(f"{nomor_hero:<3} {hero['nama']:<15} {hero['lane']:<15} {hero['role']:<12} {hero['status']:<20}")

                hapus_input = input("Pilih nomor hero yang ingin dihapus: ")
                if hapus_input in [str(n) for n in heroes]:
                    konfirmasi = input("Yakin ingin menghapus hero ini? (y) untuk menghapus: ")
                    if konfirmasi == "y":
                        del heroes[int(hapus_input)]
                        os.system('cls')
                        print("Hero berhasil dihapus.")
                        sleep(2)
                    else:
                        os.system('cls')
                        print("Penghapusan dibatalkan.")
                        sleep(2)
                else:
                    print("Nomor tidak valid.")

        # 0. Keluar
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program ini.")
            keluar = True

        else:
            print("Pilihan menu tidak valid.")