# Program untuk menentukan jenis segitiga dan menghitung luasnya
# Nama : Muhammad Bakil Amru
# NIM  : 2509106044
# POSTTEST 

# Kita mulai dengan menginput sisi-sisi segitiganya
sisi1 = float(input("masukkan sisi1 : "))
sisi2 = float(input("masukkan sisi2 : "))
sisi3 = float(input("masukkan sisi3 : "))

# kita cek apakah sisi-sisi tersebut membentuk segitiga yang seperti apa
if (sisi1 + sisi2 > sisi3) and (sisi1 + sisi3 > sisi2) and (sisi2 + sisi3 > sisi1):
     if sisi1 == sisi2 == sisi3:
       print("segitiga sama sisi")
     elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
      print("segitiga sama kaki")
     else:
       print("segitiga sembarang")

     # lalu kita lanjut menghitung luas segitiganya
     # rumus yang kita pakai adalah rumus heron agar dapat menghitung semua luas segitiganya
     # termasuk segitiga sembarang
     
     s = (sisi1 + sisi2 + sisi3) / 2
    
     luas = (s * (s - sisi1) * (s - sisi2) * (s - sisi3)) ** 0.5
     print(f"luas segitiga adalah: {luas:.2f}")
else:
    print("bukan segitiga")
# else bukan segitiga diletakkan di akhir karena jika salah satu kondisi tidak terpenuhi
# maka sudah pasti bukan segitiga, jadi tidak perlu dihitung luasnya
# END 