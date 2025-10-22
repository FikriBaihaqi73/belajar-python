# for range
# for i in range(100):
#     print("Hellow World")
#     print(i)

# mecetak angka 1 sampai 5
# for i in range(1, 6):
#     print(i)

# for i in range (10, -1, -1):
#     print("turun i", i)

# for loop dengan string

# nama = input("Masukkan nama: ")
# for huruf in nama:
#     print(huruf)

# while loop
# angka = 1
# while angka <= 5:
#     print(angka)
#     angka += 1

# password = ""
# while password != "12345":
#     password = input("Masukkan password: ")
#     if password != "12345":
#         print("Passsword salah")
# print("Password bener")

# break dan continue
# angka_rahasia = 7

# while True:
#     tebakan = int(input("Tebak angka: "))

#     if tebakan == angka_rahasia:
#         print("selamat anda benar")
#         break
#     else:
#         print("salah coba lagi")

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# loop else
# kata = input("Masukkan kata: ")
# huruf_dicari = input("Masukkan huruf yang dicari: ")

# for huruf in kata:
#     if huruf == huruf_dicari:
#         print("Huruf", huruf_dicari, "ditemukan dalam kata!", kata)
#         break
# else:
#     print("Huruf", huruf_dicari, "tidak ditemukan di kata", kata)

# while else
# password_benar = "12345"
# percobaan = 0
# max_percobaan = 3

# while percobaan < max_percobaan:
#     password = input("Masukkan password: ")
#     percobaan += 1

#     if password == password_benar:
#         print("Login berhasil")
#         break
#     else:
#         print("Password salah, sisa bercobaan", max_percobaan - percobaan)
# else:
#     print("terlalu banyak percobaan, akses ditolak")


# Nested loop
print("Tabel perkalian 1-5")
for i in range(1,6):
    for j in range (1, 6):
        hasil = i * j
        print(i, "x", j, "=", hasil)
    print("=====")