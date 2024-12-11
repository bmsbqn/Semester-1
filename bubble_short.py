def lihat_list(angka):
    print("List bilangan:")
    for i in range(5):
        print(angka[i*10:(i+1)*10])
        
def bubble_sort(angka):
    print("Proses pengurutan Bubble Sort:")
    for i in range(len(angka)):
        for j in range(len(angka) - 1 - i): 
            if angka[j] > angka[j + 1]:
                temp = angka[j]
                angka[j] = angka[j + 1]
                angka[j + 1] = temp
        print("Iterasi ke", i + 1, ":", angka)
    print("List setelah diurutkan:")
    print(angka)

angka = [12, 45, 78, 56, 34, 23, 89, 90, 67, 32,
         11, 43, 87, 65, 33, 22, 88, 92, 61, 38, 
         13, 44, 76, 54, 36, 25, 81, 95, 69, 39, 
         14, 48, 79, 58, 37, 28, 82, 96, 71, 40, 
         15, 49, 77, 53, 35, 27, 80, 94, 68, 31]

while True:
    print("\nMenu:")
    print("1. Lihat list bilangan")
    print("2. Urutkan list dengan Bubble Sort")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == "1":
        lihat_list(angka)
    elif pilihan == "2":
        bubble_sort(angka)
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan salah, coba lagi.")
