from collections import deque

antrean = deque()

def tambah_pelanggan(nama):
    antrean.append(nama)
    print(nama + " telah ditambahkan ke antrean.")

def layani_pelanggan():
    if antrean:
        pelanggan = antrean.popleft()
        print(pelanggan + " sedang dilayani.")
    else:
        print("Antrean kosong! Tidak ada pelanggan untuk dilayani.")

def tampilkan_antrean():
    if antrean:
        print("Antrean saat ini:")
        nomor = 1
        for nama in antrean:
            print(nomor, ".", nama)
            nomor += 1
    else:
        print("Antrean kosong.")

while True:
    print("\n=== SIMULASI ANTREAN PELANGGAN ===")
    print("1. Tambah Pelanggan")
    print("2. Layani Pelanggan")
    print("3. Tampilkan Antrean")
    print("4. Keluar")
    
    pilihan = input("Pilih tindakan (1-4): ")
    if pilihan == '1':
        nama = input("Masukkan nama pelanggan: ")
        tambah_pelanggan(nama)
    elif pilihan == '2':
        layani_pelanggan()
    elif pilihan == '3':
        tampilkan_antrean()
    elif pilihan == '4':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
