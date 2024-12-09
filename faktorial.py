def faktorial (n):
    if n==0 or n==1:
        return 1
    else :
        return n*(faktorial(n-1))
    
a = int(input("Masukan nilai yang akan dicari: "))
cari_faktorial=faktorial(a)
print ("Nilai dari ",a,"adalah", cari_faktorial)