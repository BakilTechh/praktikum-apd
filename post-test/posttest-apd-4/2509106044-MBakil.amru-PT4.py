import os
from time import sleep
os.system('cls' if os.name == 'nt' else 'clear')

# Program untuk menentukan jenis segitiga dan menghitung luasnya
# Nama : Muhammad Bakil Amru
# NIM  : 2509106044
# POSTTEST 4

# Sebelum menjalankan program anda akan diminta untuk login terlebih dahulu
# dengan username dan password yang anda miliki
max_percobaan = 5
username = "Bakil" # disini huruf besar dan kecilnya harus sesuai untuk dapat masuk program
password = "044"

percobaan = 0 
while percobaan < max_percobaan:
    print("Selamat datang di program menentukan jenis segitiga dan menghitung luasnya")
    # input username dan password mu , dan pastikan benar benar sama dengan yang diatas
    usn = input("masukkan username kamu : ")
    pw = input("masukkan passwordnya : ")
    if usn == username and pw == password:
        sleep(4)
        break
    # disini pastikan anda memasukkan username dan password yang benar, 
    # karena batas percobaan anda hanya 5 kali
    else:
        percobaan += 1 
        print(f"mohon cek kembali username atau password anda, sisa percobaan anda: {max_percobaan - percobaan}")
# jika sudah 5 kali maka anda akan keluar dari program
else:
    print("anda melakukan terlalu banyak percobaan, silahkan coba lagi nanti")
    exit()

# ketika sudah berhasil login, maka anda akan masuk ke menu utama
# dan anda diberi 2 pilihan yaitu menghitung luas segitiga atau keluar dari program
while True:

    print("\napa yang ingin anda lakukan?")
    print("[1] menghitung luas segitiga")
    print("[2] tidak ada dan keluar")
    pilihan = input("Pilih yang anda ingin lakukan [1/2]:") 
    # ini yang akan terjadi jika kamu memilih pilihan 1
    if pilihan == "1":  
        sisi1 = float(input("masukkan sisi1 : "))
        sisi2 = float(input("masukkan sisi2 : "))
        sisi3 = float(input("masukkan sisi3 : "))
        if (sisi1 + sisi2 > sisi3) and (sisi1 + sisi3 > sisi2) and (sisi2 + sisi3 > sisi1):
            if sisi1 == sisi2 == sisi3:
                print("segitiga sama sisi")
            elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
                print("segitiga sama kaki")
            else:
                print("segitiga sembarang")
            # selanjutnya masukkan alas dan tinggi segitiga untuk menghitung luas segitiganya 
            alas = float(input("masukkan panjang alas segitiga: "))
            tinggi = float(input("masukkan tinggi segitiga: "))
            luas =   alas * tinggi / 2

            print(f"luas segitiga adalah: {luas:.2f}")
            sleep(3)
        else:
            print("bukan segitiga")
            sleep(2)
    #jika kita memilih pilihan 2 maka kita akan berhenti dan keluar dari program
    elif pilihan == "2":
        print("terima kasih telah menggunakan program ini")
        sleep(2)
        os.system('cls')  # kita bersihkan terminal sebelum keluar
        break
    else:
        print("pilihan tidak valid, silahkan coba lagi")
        sleep(2)
