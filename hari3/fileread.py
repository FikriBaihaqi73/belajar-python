# read file

print("=== MENAMPILKAN NILAI ===")

file = open("nilai.txt", "r")

for line in file:
    data = line.strip().split(",")
    print(data[0], ":", data[1])

file.close()
print("=== Program Selesi ===")