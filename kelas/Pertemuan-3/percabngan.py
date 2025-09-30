#angka = 5

#if angka > 5:
    #print("Angka lebih besar dari 5")


# nilai = 70 

# if nilai  >= 70:
#     print("lulus")
# else:
#     print("tidak lulus")

# status = "lulus" if nilai >= 70 else "tidak lulus"
# print(status)

# usia = int(input("Masukkan usia Anda: "))

# if usia <= 0:
#     print("Usia tidak valid.")
# elif usia <= 13:
#     print("Anda adalah anak-anak.")
# elif usia <= 18:
#     print("Anda adalah remaja.")
# elif usia <= 60:
#     print("Anda adalah dewasa.")
# else: 
#     print("Anda adalah TUA.")

# nilai = int(input("Masukkan nilai Anda: "))
# if nilai >= 90:
#     print("A")
# elif nilai >= 70:
#     print("B")
# elif nilai >= 60:
#     print("C")
# elif nilai <= 60:
#     print("D")

## Nested if

# a = 2
# b = 5
# c = 6

# if a < b:
#   if a < c :
#     print ("A paling kecil")
#   else: 
#     print("C lebih kecil dari a")
# elif a<c:
#   print("c lebih besar ")
# else:
#  print("A paling besar")

nilai = int(input("massukkan nilai: "))
kelas = input("masukkan kelas: ")

if nilai >= 80 and (kelas == "A" or kelas == "a"):
  print("IPK 4")
elif nilai >= 80 and kelas == "B":
  print("IPK 3")

elif nilai >=80 and kelas == "B":
  print ("IPK 3 ")

else :
  print("IPK 3")