# read file with state

print("=== MENAMPILKAN NILAI ===")

try:
    with open("nilai.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(data[0], ":", data[1])
except FileNotFoundError:
    print("file tidak ditemukan")

print("=== Program Selesi ===")