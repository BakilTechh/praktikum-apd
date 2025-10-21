# Membuat set
# buah = {"apel", "jeruk", "mangga", "apel"}

# print(buah)

# for i in buah:
#     print(i,end=' ')

# angka = [1,1,2,5,2,3,6]

# unik = set(angka)
# print(unik)

# Daftar

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" :  {"Instagram" : "daffahrhap"
# }
# }

# # print(Biodata)
# for i,j in Biodata.items():
#     print(i)
#     print(j)

# print(f"nama saya adalah {Biodata["Mama"]}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get("Nama")}")
# print(Biodata.get("Nama"))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"}


#Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Upin Ipin" : "Comedy"})
# #Setelah Ditambah
# print(Film)

# del Film['The Conjuring']
# print(Film)

# hapus = Film.pop(['The Conjuring'])
# print(Film)
# Film.clear
# print(hapus)

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['paramore'][2][1][0])


# a = {10,11,12}
# b = {11,13,14}

# c = a | b

# print(c)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)
# {'Matematika': 80, 'B. Indonesia': 90, 'B. Inggris':
# 81}
# Nilai : 70
# {'Matematika': 80, 'B. Indonesia': 90, 'B. Inggris':
# 81, 'Kimia': 70}

# mahasiswa = [["daffa" , "dante", "bakil"]] , [["rafi" , "nuron" , ""]]
