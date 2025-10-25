def hello():
    print("kode dari function")

hello()

# functon pake parameter
def sapa(nama):
    print("halo", nama)
    print("senang bertemu")

sapa("fikri")

def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("luas dari persegi itu adalah", luas)

luas_persegi_panjang(9, 8)

def luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * radius * radius
    return luas

luas1= luas_lingkaran(7)
luas2= luas_lingkaran(21)

print("luas lingkaran radius 7:", luas1)
print("luas lingkaran radius 21:", luas2)
print("total luas keduanya:", luas1 + luas2)

# default parameter
def nyapa(nama, sapaan="halo"): #harus di akhir
    print(sapaan, nama)

nyapa("ariel")
nyapa("gaby", "hello")

# keyword argument
def perkenalan(nama, umur, kota):
    print("Nama: ", nama)
    print("Umur: " , umur)
    print("Asal: ", kota)
    print("----")

perkenalan(kota = "isekai", nama = "fikri", umur = "19")

def profil(nama, umur, kota = "Jakarta", pekerjaan = "belum bekerja"):
    print(f"=== Profil {nama.upper()} ===")
    print(f"umur: {umur} tahun")
    print(f"kota: {kota.capitalize()}")
    print(f"pekerjaan: {pekerjaan}")
    print()

# positional + keyword
profil("alice", 25) #mengggunakan default
profil("bob", 30, kota = "bandung")
profil("charlie", 28, pekerjaan = "AI Engiiner")
profil("haq", 19, pekerjaan = "Software engiiner", kota="Isekai")

# local variabel
def test():
    x = 10
    print("nilai x adalah", x)

test()
# print(x) #ini gak bisa di akses di luar

# global function
# global bisa di akses di mana saja, nilai global variabel gak bisa diubah di function kecuali jika kita menambahkan keyword global di function

nama_global = "fio"

def tampilkan_nama():
    print("Nama", nama_global)

def ubah_nama():
    global nama_global
    nama_global = "frey"
    print("nama di ubah", nama_global)

tampilkan_nama()
ubah_nama()
print(nama_global)

# parameter dinamis
# kasih * sebelum paramter itu sebagai list, kalo ** itu dictionary

def cetak_list(*list):
    for item in list:
        print(item)

cetak_list(1, 2, 3, 4, 5)

def cetak_dict(**dic):
    for key, value in dic.items():
        print(key, value)

cetak_dict(nama = "fk", umur = 19, kota = "bandung")
cetak_dict(sihir = "cahaya", kota = "isekai")