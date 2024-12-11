print ("""
DATA MAHASISWA KAMPUS IRAEEEE
=============================""")

data_mahasiswa = []
jumlah_mahasiswa = int(input("Jumlah Mahasiswa: "))
for i in range(jumlah_mahasiswa):
    print("Masukkan data mahasiswa ke-",i + 1)
    nama = input("Nama           : ")
    nim = input("NIM            : ")
    tanggal_lahir = input("Tanggal Lahir  : ")
    
    data_mahasiswa.append([nama, nim, tanggal_lahir])    
print("""
===============================
=========DATA MAHASISWA========
===============================""")
print()
for mahasiswa in data_mahasiswa:
    print("Nama             :", mahasiswa[0])
    print("NIM              :", mahasiswa[1])
    print("Tanggal Lahir    :", mahasiswa[2])
    print("=================================")