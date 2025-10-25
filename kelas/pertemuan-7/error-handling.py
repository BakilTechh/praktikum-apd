
while True:
  try :
      umur = int(input("masukkan angka : "))
      if umur <= 0:
        raise ValueError('umur tidak boleh kurang dari 0: ')
  except ValueError as  e:
    print(e)