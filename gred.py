stop = False

while not stop:

  markah_1 = input("Markah pertama: ")
  markah_2 = input("Markah kedua: ")
  markah_3 = input("Markah ketiga: ")
  markah_4 = input("Markah keempat: ")

  purata = round((int(markah_1) + int(markah_2) +  int(markah_3) + int(markah_4)) / 4)

  keputusan = "Gagal"

  if purata > 49:
    keputusan = "Lulus"

  gred = "F"

  if purata <= 49:
    gred = "E"
  elif purata <= 59:
    gred = "D"
  elif purata <= 69:
    gred = "C"
  elif purata <= 84:
    gred = "B"
  elif purata <= 100:
    gred = "A"

  print()
  print("Purata markah: " + str(purata))
  print("Keputusan: " + keputusan)
  print("Gred: " + gred)
  print()
  
  prompt = input("Hentikan program? (Taip 'y' untuk berhenti): ")

  if prompt == "y":
    stop = True
