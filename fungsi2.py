def luas_persegi_panjang (panjang, lebar) :
    return panjang*lebar

def keliling_persegi_panjang (panjang, lebar) :
    return 2*(panjang+lebar)


panjang = int(input("Masukan panjang nya manieees: "))
lebar = int(input("Masukan lebar nya manieees: "))

hasil = luas_persegi_panjang (panjang,lebar)
print ("luas persegi panjang adalah", hasil, "cm" )
hasil = keliling_persegi_panjang (panjang,lebar)
print ("Keliling persegi panjang adalah", hasil, "cm" )
