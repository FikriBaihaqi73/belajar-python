# print("hello world" syntak error
# print(nama) name error
# print(5 + "5") type eror
# angka = int("abc") value error
"""
list = [1, 2, 3]
print(list[6]) ini index eror
"""
"""
data = {"nama": "Alice"}
print(data["umur]) ini key eror
"""
# print(10 / 0) zero divison eror

# eror handling try except

# print("=== Kalkulator Sederhana ===")

# try:
#     angka1 = int(input("Masukkan angka pertama: "))
#     angka2 = int(input("Masukkan angka kedua: "))
#     hasil = angka1 / angka2
#     print("hasil", int(hasil))
# except ValueError:
#     print("Masukkan angka yang valid")
# except ZeroDivisionError:
#     print("Angka tidak bisa di bagi 0")
# except:
#     print("ada eror lain")

# print("Program selesai")

# try excpet else, else dijalankan jika tidak ada eror, kalo finally dijalankan baik itu eror atau tidak
try:
    angka = int(input("Masukkan angka: "))
except:
    print("Angka gak valid")
else:
    print("Angka yang di masukkan ", angka)
    if angka > 0:
        print("Angka positif")
    elif angka < 0:
        print("Angka Negatif")
    else:
        print("angka 0")
finally:
    print("Program selesai")
