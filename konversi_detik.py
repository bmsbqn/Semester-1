masukkan_detik = int(input("Masukkan jumlah detik: "))

jam = masukkan_detik // 3600
sisa_detik = masukkan_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print ("Hasil konversi dari", masukkan_detik, "detik adalah", jam, "jam", menit, "menit", detik, "detik.")
