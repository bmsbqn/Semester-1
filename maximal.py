def max (angka1, angka2, angka3):
    if ((angka1 > angka2) and (angka1 > angka3)):
        return angka1
    elif (angka2 > angka1) and (angka2 > angka3):
        return angka2
    else:
        return angka3

a = int(input("Masukan angka 1: "))
b = int(input("Masukan angka 2: "))
c = int(input("Masukan angka 3: "))

cek_max = max(a, b, c)
print("Nilai maksimal dari", a, ",", b, "dan", c, "adalah", cek_max)
