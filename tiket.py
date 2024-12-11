print("""
KELOMPOK VI TRAVEL
>>>>>>>>><<<<<<<<<""")
print("Kota Tujuan: ")
print("1. Surabaya")
print("2. Malang")
print("3. Bali")
print("4. Yogyakarta")
print("5. Solo")

sby = 50000
mlg = 60000
bal = 90000
yog = 90000
sol = 80000
total_harga = 0
diskon_awal = 0
diskon_tambahan = 0

kota_tujuan = input("Pilih tujuan anda: ")
jum_tiket = int(input("Jumlah pesanan: "))

if kota_tujuan == "1":
    total_harga = sby * jum_tiket
    print("Total pembayaran: Rp.", total_harga)
    if jum_tiket >= 6:
        diskon_awal = total_harga * 0.10
        total_setelah_diskon_awal = total_harga - diskon_awal
        print("Diskon 10%, total sementara: Rp.", int(total_setelah_diskon_awal))
        if jum_tiket >= 12:
            diskon_tambahan = total_setelah_diskon_awal * 0.10
            total_setelah_diskon_tambahan = total_setelah_diskon_awal - diskon_tambahan
            print("Diskon tambahan 10%, total pembayaran: Rp.", int(total_setelah_diskon_tambahan))

if kota_tujuan == "2":
    total_harga = mlg * jum_tiket
    print("Total pembayaran: Rp.", total_harga)
    if jum_tiket >= 5:
        diskon_awal = total_harga * 0.10
        total_setelah_diskon_awal = total_harga - diskon_awal
        print("Diskon 10%, total sementara: Rp.", int(total_setelah_diskon_awal))
        if jum_tiket >= 10:
            diskon_tambahan = total_setelah_diskon_awal * 0.10
            total_setelah_diskon_tambahan = total_setelah_diskon_awal - diskon_tambahan
            print("Diskon tambahan 10%, total pembayaran: Rp.", int(total_setelah_diskon_tambahan))

if kota_tujuan == "3":
    total_harga = bal * jum_tiket
    print("Total pembayaran: Rp.", total_harga)
    if jum_tiket >= 4:
        diskon_awal = total_harga * 0.10
        total_setelah_diskon_awal = total_harga - diskon_awal
        print("Diskon 10%, total sementara: Rp.", int(total_setelah_diskon_awal))
        diskon_tambahan = total_setelah_diskon_awal * 0.10
        total_setelah_diskon_tambahan = total_setelah_diskon_awal - diskon_tambahan
        print("Diskon tambahan 10%, total pembayaran: Rp.", int(total_setelah_diskon_tambahan))

if kota_tujuan == "4":
    total_harga = yog * jum_tiket
    print("Total pembayaran: Rp.", total_harga)
    if jum_tiket >= 4:
        diskon_awal = total_harga * 0.10
        total_setelah_diskon_awal = total_harga - diskon_awal
        print("Diskon 10%, total sementara: Rp.", int(total_setelah_diskon_awal)) 
        diskon_tambahan = total_setelah_diskon_awal * 0.10
        total_setelah_diskon_tambahan = total_setelah_diskon_awal - diskon_tambahan
        print("Diskon tambahan 10%, total pembayaran: Rp.", int(total_setelah_diskon_tambahan))

if kota_tujuan == "5":
    total_harga = sol * jum_tiket
    print("Total pembayaran: Rp.", total_harga)
    if jum_tiket >= 4:
        diskon_awal = total_harga * 0.10
        total_setelah_diskon_awal = total_harga - diskon_awal
        print("Diskon 10%, total sementara: Rp.", int(total_setelah_diskon_awal))
        diskon_tambahan = total_setelah_diskon_awal * 0.10
        total_setelah_diskon_tambahan = total_setelah_diskon_awal - diskon_tambahan
        print("Diskon tambahan 10%, total pembayaran: Rp.", int(total_setelah_diskon_tambahan))

