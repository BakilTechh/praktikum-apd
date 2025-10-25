# POSTTEST 7
# MUHAMMAD BAKIL AMRU 
# 2509106044
# SET AND DICTIONARY 

import os
from time import sleep
os.system('cls')

# === DATA GLOBAL ===
Orang = {
    "bakil": {"password": "admin#1234", "role": "admin"},
    "tikus": {"password": "tikusberdasi", "role": "member"}
}

heroes = {
    1: {"nama": "Angela", "lane": "Mid Lane", "role": "Support", "status": "Auto ban"},
    2: {"nama": "Yi-Shun-shin", "lane": "Jungler", "role": "Assasin", "status": "Auto ban"},
    3: {"nama": "Diggie", "lane": "Roaming", "role": "Support", "status": "Wajib pick"},
    4: {"nama": "Natan", "lane": "Gold Lane", "role": "Marksman", "status": "Auto ban"},
    5: {"nama": "Bane", "lane": "Exp Lane", "role": "Fighter", "status": "Auto ban"},
}

lanes = ["Jungler", "Roaming", "Exp", "Gold", "Mid"]
roles_hero = ["Tank", "Fighter", "Assasin", "Marksman", "Mage", "Support"]
status_hero = ["Auto ban", "Wajib pick",]

role = None
username = None

# === FUNGSI DAN PROSEDUR ===

def tampilkan_semua_hero():
    print("=" * 70)
    print(f"{'No':<3} {'Hero':<15} {'Lane':<15} {'Role':<12} {'Status':<20}")
    print("=" * 70)
    for nomor_hero, hero in heroes.items():
        print(f"{nomor_hero:<3} {hero['nama']:<15} {hero['lane']:<15} {hero['role']:<12} {hero['status']:<20}")

def jumlah_hero():
    print(f"\nJumlah hero saat ini: {len(heroes)}")

def tampilkan_hero_berdasarkan_lane(lane):
    print(f"\nHero di lane {lane}:")
    for hero in heroes.values():
        if hero["lane"] == lane:
            print(f"- {hero['nama']} ({hero['role']})")

def cari_hero_berstatus(status):
    print(f"\nHero dengan status {status}:")
    for hero in heroes.values():
        if hero["status"] == status:
            print(f"- {hero['nama']} ({hero['lane']})")

def tambah_hero():
    nama = input("Nama Hero: ")
    if any(char in "0123456789" for char in nama):
        print("Nama tidak boleh mengandung angka.")
        return

    # Pilihan Lane
    print("\nPilih Lane:")
    for i in range(len(lanes)):
        print(f"{i+1}. {lanes[i]} Lane")
    try:
        lane_input = int(input("Masukkan nomor lane (1–5): "))
        lane = lanes[lane_input - 1] + " Lane"
    except:
        print("Anda menggunakan input yang salah, harus menggunakan angka yang tertera.")
        return

    # Pilihan Role
    print("\nPilih Role:")
    for i in range(len(roles_hero)):
        print(f"{i+1}. {roles_hero[i]}")
    try:
        role_input = int(input("Masukkan nomor role (1-6): "))
        role_hero = roles_hero[role_input - 1]
    except:
        print("Input role tidak valid.")
        return

    # Pilihan Status
    print("\nPilih Status:")
    for i in range(len(status_hero)):
        print(f"{i+1}. {status_hero[i]}")
    try:
        status_input = int(input("Masukkan nomor status (1-2): "))
        status = status_hero[status_input - 1]
    except:
        print("Anda menggunakan input yang salah, harus menggunakan angka yang tertera.")
        return

    # Menentukan nomor hero baru
    nomor_tertinggi = 0
    for nomor in heroes:
        if nomor > nomor_tertinggi:
            nomor_tertinggi = nomor
    nomor_baru = nomor_tertinggi + 1

    # Menambahkan ke dictionary
    heroes[nomor_baru] = {
        "nama": nama,
        "lane": lane,
        "role": role_hero,
        "status": status
    }
    print("Hero berhasil ditambahkan.")
    

def hapus_hero():
    if len(heroes) == 0:
        print("Belum ada hero untuk dihapus.")
        return

    print("\nDAFTAR HERO:")
    tampilkan_semua_hero()

    hapus_input = input("Masukkan nomor hero yang ingin dihapus: ")

    try:
        nomor = int(hapus_input)
        if nomor in heroes:
            hero = heroes[nomor]
            print(f"\nKamu akan menghapus hero: {hero['nama']} ({hero['lane']} - {hero['role']} - {hero['status']})")
            konfirmasi = input("Yakin ingin menghapus hero ini? (y/Y untuk hapus): ")
            if konfirmasi.lower() == "y":
                del heroes[nomor]
                print("Hero berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
        else:
            print("Nomor hero tidak ditemukan.")
    except:
        print("Anda menggunakan input yang salah, harus menggunakan angka yang tertera.")

def ubah_hero():
    if len(heroes) == 0:
        print("Belum ada hero untuk diubah.")
        return

    print("\nDAFTAR HERO:")
    tampilkan_semua_hero()

    ubah_input = input("Masukkan nomor hero yang ingin diubah: ")

    try:
        nomor = int(ubah_input)
        if nomor not in heroes:
            print("Nomor hero tidak ditemukan.")
            return
    except:
        print("Input tidak valid. Harus berupa angka.")
        return

    nama = input("Nama Hero Baru: ")
    if any(char in "0123456789" for char in nama):
        print("Nama tidak boleh mengandung angka.")
        return

    # Pilihan Lane
    print("\nPilih Lane:")
    for i in range(len(lanes)):
        print(f"{i+1}. {lanes[i]} Lane")
    try:
        lane_input = int(input("Masukkan nomor lane (1–5): "))
        lane = lanes[lane_input - 1] + " Lane"
    except:
        print("Input lane tidak valid.")
        return

    # Pilihan Role
    print("\nPilih Role:")
    for i in range(len(roles_hero)):
        print(f"{i+1}. {roles_hero[i]}")
    try:
        role_input = int(input("Masukkan nomor role (1–6): "))
        role_hero = roles_hero[role_input - 1]
    except:
        print("Input role tidak valid.")
        return

    # Pilihan Status
    print("\nPilih Status:")
    for i in range(len(status_hero)):
        print(f"{i+1}. {status_hero[i]}")
    try:
        status_input = int(input("Masukkan nomor status (1–5): "))
        status = status_hero[status_input - 1]
    except:
        print("Input status tidak valid.")
        return

    heroes[nomor] = {
        "nama": nama,
        "lane": lane,
        "role": role_hero,
        "status": status
    }
    print("Hero berhasil diubah.")
    
# konfirmasi jika pilihan 0
def hitung_mundur(n):
    if n == 0:
        print("Program akan disiapkan untuk keluar...\n")
        sleep(2)
    else:
        print(f"Keluar dalam {n} detik...")
        sleep(1)
        hitung_mundur(n - 1)  # BAGIAN REKURSIFNYA

def konfirmasi_keluar():
    pilihan = input("Yakin ingin keluar? (y/Y untuk keluar): ")
    if pilihan.lower() == "y":
        hitung_mundur(3)  # Fungsi rekursifnya dipanggil di sini
        print("Baik, sampai jumpa", username, f"({role})", "kami tunggu update hero selanjutnya")
        return True
    else:
        print("Kembali ke menu.")
        return False
      
# === KITA AKAN LOGIN KE MENU UTAMA ===

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
        sleep(2)
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

# === MENU UTAMA ===
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
            sleep(1)
            if len(heroes) == 0:
                print("Tidak ada hero yang overpowered.")
            else:
                tampilkan_semua_hero()
                sleep(1)
                jumlah_hero()
                sleep(1)
                print("\n== BAGIAN LANE DARI HERONYA==")
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
                print()
                print("== BAGIAN STATUS DARI HERONYA==")
                cari_hero_berstatus("Auto ban")
                sleep(1)
                cari_hero_berstatus("Wajib pick")
                sleep(1)
                print()
                print("List ini adalah update patch terbaru dari hero-hero yang wajib pick/ban di Mobile Legends(PATCH OKTOBER AKHIR).")
            sleep(2)

        # 2. Menambahkan Hero
        elif pilihan == "2" and role == "admin":
            os.system('cls')
            tambah_hero()
            sleep(2)

        # 3. Mengubah Hero
        elif pilihan == "3" and role == "admin":
            os.system('cls')
            ubah_hero()
            sleep(2)

        # 4. Menghapus Hero
        elif pilihan == "4" and role == "admin":
            os.system('cls')
            hapus_hero()
            sleep(2)

        # 0. Keluar
        elif pilihan == "0":
            keluar = konfirmasi_keluar()

        # Jika input tidak valid
        else:
            print("Pilihan menu tidak valid.")
            sleep(2)