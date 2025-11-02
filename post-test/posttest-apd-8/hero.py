import os
from time import sleep
from prettytable import PrettyTable
from data import heroes, lanes, roles_hero, status_hero

# === FUNGSI DAN PROSEDUR ===

def tampilkan_semua_hero():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Hero", "Lane", "Role", "Status"]
    for nomor_hero, hero in heroes.items():
        tabel.add_row([nomor_hero, hero["nama"], hero["lane"], hero["role"], hero["status"]])
    print(tabel)

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
    nomor_tertinggi = max(heroes.keys(), default=0)
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
            print("1. Ya, hapus hero ini")
            print("2. Ga, gajadi deh")
            konfirmasi = input("Masukkan pilihan (1/2): ")
            if konfirmasi == "1":
                del heroes[nomor]
                sleep(2)
                os.system('cls')
                print("Hero berhasil dihapus.")
                sleep(1)
            else:
                print("Penghapusan dibatalkan.")
        else:
            print("Nomor hero tidak ditemukan.")
    except:
        print("Input tidak valid. Harus berupa angka.")
        return

    # Konfirmasi untuk menghapus lagi (rekursif)
    print("\nApakah kamu ingin menghapus hero lainnya?")
    print("1. Ya, lanjut hapus")
    print("2. Ga, gaada.")
    ulang = input("Masukkan pilihan (1/2): ")
    if ulang == "1":
        os.system('cls')
        hapus_hero()
    else:
        os.system('cls')
        print("Kembali ke menu utama.")

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
        status_input = int(input("Masukkan nomor status (1–2): "))
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