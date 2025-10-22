nama = " muhammad fikri baihaqi "
umur = 19

# pesan = "nama saya, " + nama + "umur saya, " + umur
# print(pesan) salah karena string gak bisa di gabung int

pesan = "nama saya, " + nama + " umur saya " + str(umur)
print(pesan)
print(len(nama))
print(len(pesan))

# cara ngambil karakter dari string
print(nama[2])
print(nama[-2])

# string slicing
print(nama[:])
print(nama[2:])
print(nama[2:6])

# string method
print(nama.upper()) # jadi gede semua
print(nama.lower()) # jadi kcil semua
print(nama.title()) # jadi gede huruf awal setiap kata
print(nama.capitalize()) # jadi gde huruf awalnya
print(nama.strip()) # menghapus spasi di awal dan akhir
print(nama.replace("muhammad", "m")) # mengganti kata
print(nama.count("a")) # menghitng jumlah huruf
print(nama.find("fikri")) # menemukan kata

# escape character
print("baris 1\nbaris 2") # new line
print("Maou\t73") #tab
print("Users\\Desktop\\file.txt") #backslash
print("Dia berkata \"hello\" kepada saya")

# string interpolation
nama = "Baihaqi"
umur = 19
kota = "Jakarta"

profil= f"Halo nama saya {nama}, umur saya {umur} tahun, asal kota saya {kota}"
print(profil)

# bisa menambahkan expression
harga = 30000
jumlah = 4
total = f"total harga yang harus dibayar adalah : {harga * jumlah:,}".replace(",", ".")
print(total)

kalimat = f"Halo {nama.upper()}"
print(kalimat)