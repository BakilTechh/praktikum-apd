# POSTTEST 2
# Nama : Muhammad Bakil Amru
# NIM  : 2509106044


# Data awal yang kita miliki
tinggi = 144
Berat = 210.2
Nama = "Sahroni"
Kebenaran = True

# Print atau Tampilkan data awal beserta tipe datanya
print("Data awal:")
print("data ke 1 =", tinggi, "adalah tipe", type(tinggi))
print("data ke 2 =", Berat, "adalah tipe", type(Berat))
print("data ke 3 =", Nama, "adalah tipe", type(Nama))
print("data ke 4 =", Kebenaran, "adalah tipe", type(Kebenaran))

# Kita ubah tipe data tersebut satu per satu
tinggi_baru = str(tinggi)
Berat_baru = int(Berat)
Nama_baru = list(Nama)
Kebenaran_baru = float(Kebenaran)

# Tampilkan data data tersebut yang sudah diubah 
print("\nData setelah diubah:")
print("data ke 1 =", tinggi_baru, "sekarang bertipe", type(tinggi_baru))
print("data ke 2 =", Berat_baru, "sekarang bertipe", type(Berat_baru))
print("data ke 3 =", Nama_baru, "sekarang bertipe", type(Nama_baru))
print("data ke 4 =", Kebenaran_baru, "sekarang bertipe", type(Kebenaran_baru))

#  Selanjutnya tampilkan jumlah nilai int dan float secara manual
print("\nJumlah nilai bertipe int dan float sebelum diubah: 144 + 210.2 + True = 355.2")
print("Jumlah nilai bertipe int dan float setelah diubah: 210 + 1.0 = 211.0")