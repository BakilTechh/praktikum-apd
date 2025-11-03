import os
from time import sleep
from prettytable import PrettyTable
import inquirer  
from data import heroes, lanes, roles_hero, status_hero

# === FUNGSI DAN PROSEDUR ===

def tampilkan_semua_hero():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Hero", "Lane", "Role", "Status"]
    for i, hero in enumerate(heroes.values(), start=1):
        tabel.add_row([i, hero["nama"], hero["lane"], hero["role"], hero["status"]])
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
    print()

    # Pilih Lane
    lane = inquirer.prompt([
        inquirer.List("lane", message="Pilih Lane Hero", choices=[f"{l} Lane" for l in lanes])
    ])["lane"]

    # Pilih Role
    role_hero = inquirer.prompt([
        inquirer.List("role", message="Pilih Role Hero", choices=roles_hero)
    ])["role"]

    # Pilih Status
    status = inquirer.prompt([
        inquirer.List("status", message="Pilih Status Hero", choices=status_hero)
    ])["status"]

    nomor_tertinggi = max(heroes.keys(), default=0)
    nomor_baru = nomor_tertinggi + 1

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

    # Buat mapping dari urutan tampil ke key asli
    hero_keys = list(heroes.keys())

    print("\nDAFTAR HERO:")
    tabel = PrettyTable()
    tabel.field_names = ["No", "Hero", "Lane", "Role", "Status"]
    for i, key in enumerate(hero_keys, start=1):
        hero = heroes[key]
        tabel.add_row([i, hero["nama"], hero["lane"], hero["role"], hero["status"]])
    print(tabel)

    hapus_input = input("Masukkan nomor hero yang ingin dihapus: ")
    try:
        nomor_tampil = int(hapus_input)
        if 1 <= nomor_tampil <= len(hero_keys):
            key_asli = hero_keys[nomor_tampil - 1]
            hero = heroes[key_asli]

            print(f"\nKamu akan menghapus hero: {hero['nama']} ({hero['lane']} - {hero['role']} - {hero['status']})")
            konfirmasi = inquirer.prompt([
                inquirer.List("konfirmasi", message="Konfirmasi penghapusan", choices=["Ya", "Tidak"])
            ])["konfirmasi"]

            if konfirmasi == "Ya":
                del heroes[key_asli]
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

    ulang = inquirer.prompt([
        inquirer.List("ulang", message="Hapus hero lain?", choices=["Ya", "Tidak"])
    ])["ulang"]
    if ulang == "Ya":
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

    lane = inquirer.prompt([
        inquirer.List("lane", message="Pilih Lane Baru", choices=[f"{l} Lane" for l in lanes])
    ])["lane"]

    role_hero = inquirer.prompt([
        inquirer.List("role", message="Pilih Role Baru", choices=roles_hero)
    ])["role"]

    status = inquirer.prompt([
        inquirer.List("status", message="Pilih Status Baru", choices=status_hero)
    ])["status"]

    heroes[nomor] = {
        "nama": nama,
        "lane": lane,
        "role": role_hero,
        "status": status
    }
    print("Hero berhasil diubah.")