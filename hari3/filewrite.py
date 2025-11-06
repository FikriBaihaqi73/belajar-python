# write file 

print("=== SIMPAN DATA NILAI ===")

file = open("nilai.txt", "w")

while True:
    nama = input("Nama Siswa (Enter untuk selesai): ")
    if nama == "":
        break
    
    nilai = input("nilai siswa: ")

    file.write(nama + "," + nilai + "\n")
    print("Data", nama, "tersimpan")

file.close()
print("Program selesai")