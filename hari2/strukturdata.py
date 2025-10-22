# list, bisa menyimpan data dalam 1 variabel ditulis []

# kosong
daftar_kosong = []
print(daftar_kosong)
# list angka
angka = [1, 2, 3, 4, 5]
print(angka)
# list string
nama = ["baihaqi", "fikri", "fio"]
print(nama)
# list campuran
campuran = ["fikri", 73, "fio", 24]
print(campuran)

# manipulasi list
"""
nambah elemen pakai append(data)-> diahkhir, kalo insert(index, data) sesuai index yang dipiluh
hapus data pakai remove(data), atau pop() untuk hapus elemen akhir, pakai del misalnya mau sesuai index
hitung panjanh list pakai len(list)
bisa di gabung denghan list lain pakai +
"""
buah = ["apel", "jeruk", "pisang", "mangga"]
print(buah[0])
print(buah[1])

warna = ["merah", "biru", "hijau"]
warna[1] = "kuning"
print(warna)

anime = ["tensura", "opm"]
print(anime)
anime.append("naruto") #nambah ke akhir
print(anime)
anime.insert(0, "doraemon") #nambah sesuai index
print(anime)
anime.remove("opm") #hapus sesuai data
print(anime)
anime.pop() # hapus paling akhir
print(anime)
del anime[0] #hapus pakai index
print(anime)

mobil = ["inova", "alya", "sigra"]
print(len(mobil))

satu = [1, 2, 3, 4, 5]
dua = [6, 7, 8, 9, 10]
gabungan = satu + dua
print(gabungan)

for m in mobil:
    print(m)

for i in range(0, len(mobil)):
    print(mobil[i])

if "sigra" in mobil:
    print("ada sigra")
else:
    print("buah tidak ada")


# tuple sama kaya list tapi dia gak bisa di ubah pakai tanda ()
point = (5, 10)
print(point[0])

tanggal_lahir = (19, 3, 2006)
print(tanggal_lahir)

for t in tanggal_lahir:
    print(t)

# Dictionary menyimpan data dari key-value pakai {}, del untuk hapus data, len untuk cek panjang

data = {
    "nama" : "Fikri",
    "umur" : 19,
    "jurusan" : "programmer"
}
print(data)
print(data["nama"])
print(data["jurusan"])
print(data["umur"])
# ubah nilai
data["jurusan"] = "teknik sihir"
print(data["jurusan"])
# hapus key-value
del data["jurusan"]
print(data)
# perulanhan
for key in data:
    print(key, data[key])
# pakai key value
for key, value in data.items():
    print(key, value)

# set(himpuan) itu adalah data yang tidak berurutan, dan tidak ada data yang duplikat, oakai {} atau set()

sihir = {"api", "air", "tanah"}
print(sihir)
sihir.add("cahaya")
sihir.add("cahaya")
print(sihir)
sihir.remove("tanah")
print(sihir)

for s in sihir:
    print(s)