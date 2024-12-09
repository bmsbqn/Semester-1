
undo_stack = []
redo_stack = []

def tindakan (item):
    undo_stack.append(item)
    redo_stack.clear()
    print ("Item yang dimasukkan =>", item)

def undo():
    if undo_stack:
        item = undo_stack.pop()
        redo_stack.append(item)
        print ("Undo =>", item)
    else:
        print ("Tidak ada tindakan yang bisa dilakukan!")

def redo():
    if redo_stack:
        item = redo_stack.pop()
        undo_stack.append(item)
        print ("Redo =>", item)
    else:
        print ("Tidak ada tindakan yang bisa dilakukan!")

def hasil_stack():
    print ("Undo Stack =>", undo_stack)
    print ("Redo Stack =>", redo_stack)  

while True:
    print ()
    print ("Uji coba Program Undo dan Redo")
    print ("==============================")
    print ("1. Masukan item uji coba")
    print ("2. Tindakan Undo")
    print ("3. Tindakan Redo")
    print ("4. Tampilkan Stack")
    print ("5. Keluar")
    
    pilihan = input("Pilih Tindakan (1-5): ")
    if pilihan == '1':
        item = input ("Masukan item uji coba => ")
        tindakan (item)
    elif pilihan == '2' :
        undo ()
    elif pilihan == '3' :
        redo ()
    elif pilihan == '4' :
        hasil_stack()
    elif pilihan == '5' :
        print ("Keluar dari program")
        break
    else :
        print ("Pilihan tidak ada dalam daftar!")
