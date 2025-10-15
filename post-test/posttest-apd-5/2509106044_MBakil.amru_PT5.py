# Muhammad Bakil Amru
# 2509106044
# POSTTEST 5

# Untuk clear terminal 
import os

# Data Orang yang boleh login: [username, password, role]

Orang = [
    ["bakil", "admin#1234", "admin"],
    ["member", "member#1234", "member"]
]

# List hero wajib pick/bannya: [Nama Hero, Lane, Role, Status]

heroes = [
    ["Angela", "Mid Lane", "Support", "Auto ban"],
    ["Yi-Shun-shin", "Jungler", "Assasin", "Auto ban"],
    ["Diggie", "Roaming", "Support", "Wajib pick"],
    ["Natan", "Gold Lane", "Marksman", "Auto ban"],
    ["Bane", "Exp Lane", "Fighter", "Broken"]
]

# Ini lane lane untuk hero mobile legend

lanes = ["Jungler","Roaming","Exp","Gold","Mid"]

# Role masing masing hero mobile legends

roles_hero = ["Tank", "Fighter", "Assasin", "Marksman", "Mage", "Support"]

# Status dari hero heronya

status_hero = ["Auto ban", "Wajib pick", "Broken", "Meta", "Situasional"]

#  Sebelum masuk program, memastikan siapa yang login

#  Role apa saja jika masuk dalam program akan menampilkan 

role = None
username = None

while True:
    os.system('cls')
    print("=== Selamat datang di program Tier list Hero Wajib pick/ban untuk hero Mobile Legends ===")
    print("Siapa yang ingin login?")
    print("1. Admin")
    print("2. Member")
    print("3. Mendaftar sebagai member")
    pilihan_login = input("Masukkan pilihan (1/2/3): ")

    # Memastikan user memilih atau hanya menginput 1, 2, atau 3
    if pilihan_login not in ["1", "2", "3"]:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.\n")
        continue  # kembali ke atas loop

    # kita lanjut ke bagian login

    if pilihan_login == "1" or pilihan_login == "2":
        username = input("Username: ")
        password = input("Password: ")

        login_berhasil = False
        for user in Orang:
            if user[0] == username and user[1] == password:
                if pilihan_login == "1" and user[2] == "admin":
                    role = "admin"
                    login_berhasil = True
                    break
                elif pilihan_login == "2" and user[2] == "member":
                    role = "member"
                    login_berhasil = True
                    break

        if login_berhasil:
            print("Login berhasil sebagai", username, f"({role})")
            break
        else:
            print("Username atau password salah, atau role tidak sesuai.\n")

    elif pilihan_login == "3":
        print("\n=== Hai member baru, buat dulu username dan password mu ===")
        username_baru = input("Masukkan username baru: ")
        password_baru = input("Masukkan password baru: ")

        # Cek apakah username sudah dipakai
        sudah_ada = False
        for user in Orang:
            if user[0] == username_baru:
                sudah_ada = True
                break

        if sudah_ada:
            print("Username sudah dipakai. Silakan pilih yang lain.\n")
        else:
            Orang.append([username_baru, password_baru, "member"])
            print("Registrasi berhasil! Silakan login sebagai member.\n")

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.\n")


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
                nomor = 1
                for hero in heroes:
                    print(f"{nomor:<3} {hero[0]:<15} {hero[1]:<15} {hero[2]:<12} {hero[3]:<20}")
                    nomor += 1

        # 2. Menambahkan Hero
        elif pilihan == "2" and role == "admin":
            os.system('cls')
            nama = input("Nama Hero: ")

            # kita pastikan user jangan memasukkan angka pada nama hero karena hero mobile legend tidak ada yang
            # memiliki angka di namanya

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

                if lane_input == "1":
                    lane = lanes[0] + " Lane"
                elif lane_input == "2":
                    lane = lanes[1] + " Lane"
                elif lane_input == "3":
                    lane = lanes[2] + " Lane"
                elif lane_input == "4":
                    lane = lanes[3] + " Lane"
                elif lane_input == "5":
                    lane = lanes[4] + " Lane"
                else:
                    print("Pilihan lane tidak valid.")
                    lane = None

                if lane:
                    print("\nPilih Role:")
                    print("1. Tank\n2. Fighter\n3. Assasin\n4. Marksman\n5. Mage\n6. Support")
                    role_input = input("Masukkan nomor role: ")

                    if role_input == "1":
                        role_hero = roles_hero[0]
                    elif role_input == "2":
                        role_hero = roles_hero[1]
                    elif role_input == "3":
                        role_hero = roles_hero[2]
                    elif role_input == "4":
                        role_hero = roles_hero[3]
                    elif role_input == "5":
                        role_hero = roles_hero[4]
                    elif role_input == "6":
                        role_hero = roles_hero[5]
                    else:
                        print("Pilihan role tidak valid.")
                        role_hero = None

                    if role_hero:
                        print("\nPilih Status:")
                        print("1. Auto ban\n2. Wajib pick\n3. Broken\n4. Meta\n5. Situasional")
                        status_input = input("Masukkan nomor status: ")

                        if status_input == "1":
                            status = status_hero[0]
                        elif status_input == "2":
                            status = status_hero[1]
                        elif status_input == "3":
                            status = status_hero[2]
                        elif status_input == "4":
                            status = status_hero[3]
                        elif status_input == "5":
                            status = status_hero[4]
                        else:
                            print("Pilihan status tidak valid.")
                            status = None

                if status:
                    heroes.append([nama, lane, role_hero, status])
                    print("Hero berhasil ditambahkan.")

        elif pilihan == "3" and role == "admin":
            os.system('cls')
            if len(heroes) == 0:
                print("Belum ada hero untuk diubah.")
            else:
                print("\nDAFTAR HERO:")
                print("=" * 70)
                print(f"{'No':<3} {'Hero':<15} {'Lane':<15} {'Role':<12} {'Status':<20}")
                print("=" * 70)
                nomor = 1
                for hero in heroes:
                    print(f"{nomor:<3} {hero[0]:<15} {hero[1]:<15} {hero[2]:<12} {hero[3]:<20}")
                    nomor += 1

                ubah_hero = input("Pilih nomor hero yang ingin kamu ubah: ")
                if ubah_hero in [str(i) for i in range(1, len(heroes)+1)]:
                    ubah = int(ubah_hero)

                    # disini juga pastikan user tidak menginput angka untukk nama hero mobile legends

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

                        if lane_input == "1":
                            lane = lanes[0] + " Lane"
                        elif lane_input == "2":
                            lane = lanes[1] + " Lane"
                        elif lane_input == "3":
                            lane = lanes[2] + " Lane"
                        elif lane_input == "4":
                            lane = lanes[3] + " Lane"
                        elif lane_input == "5":
                            lane = lanes[4] + " Lane"
                        else:
                            print("Pilihan lane tidak valid.")
                            lane = None

                        if lane:
                            print("\nPilih Role:")
                            print("1. Tank\n2. Fighter\n3. Assasin\n4. Marksman\n5. Mage\n6. Support")
                            role_input = input("Masukkan nomor role: ")

                            if role_input == "1":
                                role_hero = roles_hero[0]
                            elif role_input == "2":
                                role_hero = roles_hero[1]
                            elif role_input == "3":
                                role_hero = roles_hero[2]
                            elif role_input == "4":
                                role_hero = roles_hero[3]
                            elif role_input == "5":
                                role_hero = roles_hero[4]
                            elif role_input == "6":
                                role_hero = roles_hero[5]
                            else:
                                print("Pilihan role tidak valid.")
                                role_hero = None

                            if role_hero:
                                print("\nPilih Status:")
                                print("1. Auto ban\n2. Wajib pick\n3. Broken\n4. Meta\n5. Situasional")
                                status_input = input("Masukkan nomor status: ")

                                if status_input == "1":
                                    status = status_hero[0]
                                elif status_input == "2":
                                    status = status_hero[1]
                                elif status_input == "3":
                                    status = status_hero[2]
                                elif status_input == "4":
                                    status = status_hero[3]
                                elif status_input == "5":
                                    status = status_hero[4]
                                else:
                                    print("Pilihan status tidak valid.")
                                    status = None

                                if status:
                                    heroes[ubah - 1] = [nama, lane, role_hero, status]
                                    print("Hero berhasil diubah.")
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

                nomor = 1
                for hero in heroes:
                    print(f"{nomor:<3} {hero[0]:<15} {hero[1]:<15} {hero[2]:<12} {hero[3]:<20}")
                    nomor += 1

                hapus_input = input("Pilih nomor hero yang ingin kamu hapus: ")

        # Validasi input sebagai string angka yang cocok dengan nomor hero
                if hapus_input in [str(i) for i in range(1, len(heroes)+1)]:
                    hapus = int(hapus_input)

                    konfirmasi = input(f"Yakin ingin menghapus hero '{heroes[hapus - 1][0]}'? (y/Y untuk ya): ")
                    if konfirmasi == "y" or konfirmasi == "Y":
                        heroes.pop(hapus - 1)
                        print("Hero berhasil dihapus.")
                    else:
                        print("Penghapusan dibatalkan.")
                else:
                    print("Nomor tidak valid.")

        # 0. Keluar 
        elif pilihan == "0":
            keluar = True # jika kita keluar maka
            print("Terima kasih", role , "kita akan menunggu update hero broken lainnya")

        # jika salah input
        else:
            print("Pilihan tidak valid atau akses ditolak.")