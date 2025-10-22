# operator aritmatika
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a // b)
print(a % b)

print(a**3)

# operator assigment and compound
x = 10
print("x awal adalh", x)

x += 5
print("hasil dari +=5", x)

x -= 3
print(x)

x *= 3
print(x)

x /= 3
print(int(x))

# operator perbandingan
"""
 a > b ini lebh besar
 a < b ini lebih kecil
 a >= ini lebih besar sama dengan
 a <= ini lebih kecil sama dengan
 a == sama dengan
 a !=b ini tidak sama dengan
"""

nama1 = "Alice"
nama2 = "Bob"
nama3 = "Alice"

print(nama1 == nama3)
print(nama1 == nama2)
print(nama1 != nama2)

# operator logika
umur = 25
print(umur > 18 and umur <30)

hari = "Sabtu"
print(hari == "Sabtu" or hari == "Minggu")

aktif = True
print(not aktif)

# operator string
nama_depan = "Muhammad"
nama_belakang = "Fikri"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

kata = "hello"
print(kata * 3)

garis = "-"
print(garis * 30)

kalimat = "Python adalah bahasa ular"
print("Python" in kalimat)
print("PHP" in kalimat)
print("adalah" in kalimat)

# prioritas
"""
*** (pangkat)
*,/,//,%(perkalian , pembagian)
+,-(penjumlahan, pengurangan)
==,!=,<,>,<=,>=(perbandingan)
not logika
and logika
or logika
"""