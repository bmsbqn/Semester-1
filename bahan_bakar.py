kelas_stock = 3  
kelas_sp = 4     
kelas_pro = 5    


bahan_bakar_awal = 100
isi_bensin = 5  

print ("""
================================       
======= KELOMPOK VI RACE =======
================================""")
print("Pilih kelas kendaraan:")
print("1. Kelas Stock")
print("2. Kelas Semi Pro")
print("3. Kelas Profesional")
pilihan = input("Masukkan nomor kelas (1-2-3): ")

if pilihan == "1":
    konsumsi_bahan_bakar = kelas_stock
    kelas = "Stock"
elif pilihan == "2":
    konsumsi_bahan_bakar = kelas_sp
    kelas = "Semi Pro"
elif pilihan == "3":
        konsumsi_bahan_bakar = kelas_pro
        kelas = "Profesional"

bahan_bakar = bahan_bakar_awal
putaran = 0
counter = 0

while bahan_bakar >= konsumsi_bahan_bakar:
    bahan_bakar -= konsumsi_bahan_bakar
    putaran += 1
    counter += 1

    if counter == 5:
        bahan_bakar += isi_bensin
        counter = 0
        
print("Putaran yang dapat ditempuh untuk kelas",kelas,":", putaran)