# angka = int(input("Masukkan angka: "))

# if angka > 0:
#     print("Angka positif")
# if angka < 0:
#     print("Angka negatif")
# if angka == 0 :
#     print( f"angka {angka}")

# nilai = int(input("Masukkan nilai: "))

# # if nilai >= 60:
# #     print("Anda lulus")
# # else:
# #     print("Anda tidak lulus")

# if nilai >=90:
#     print("Grade kamu A")
# elif nilai >=80:
#     print("Grade kamu B")
# elif nilai >=70:
#     print("Grade kamu C")
# elif nilai >=60:
#     print("Grade kamu D")
# else:
#     print("Grade kamu E tidak lulus")

# # kondisi dengan operator logika
# umur = int(input("Masukkan umur: "))
# sim = input("Apakah punya sim?(y/n) ")

# if umur >= 17 and sim == "y":
#     print("boleh mengendarai motor")
# else:
#     print("Tidak boleh mengendarai motor")

# nested if
# username = input("Masukkan Username: ")
# pw = input("Masukkan password: ")

# if username == "Admin":
#     if pw == "Admin123#":
#         print("selamat datang admin")
#     else:
#         print("pw salah")
# else:
#     print("username tidak ditemukan")

# match case


# hari = input("Masukkan hari: ").lower()

# match hari:
#     case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
#         print("Hari kerja")
#     case "sabtu" | "minggu":
#         print("hari libur")
#     case _:
#         print("hari tidak sesuai")

# ternary operator

angka = int(input("Masukkan angka: "))

hasil = "Positif" if angka > 0 else "Negatif"
print(hasil)
