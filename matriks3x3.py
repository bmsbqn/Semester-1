# inisiasi list
A = [[1,1,2],[2,3,2],[1,2,1]]
B = [[2,1,2],[4,3,2],[3,2,1]]

#inisiasi hasil perkalian matrix
C = []
D = []
E = []
F = []
G = []
H = []
I = []
J = []
K = []

#mengetahui baris dan kolom matriks
Baris_A =len(A)
Kolom_A =len(A[0])

Baris_B =len(B)
Kolom_B =len(B[0])

# cetak details matriks
print (A)
print("baris matriks A adalah", Baris_A)
print("kolom matriks A adalah",Kolom_A)

print (B)
print("baris matriks B adalah", Baris_B)
print("kolom matriks B adalah",Kolom_B)

#cek kondisi matriks untuk perkalian
if (Kolom_A !=Baris_B):
    print ("Matriks A dengan B tidak dapat dikalikan")
else:
    print ("matriks A dengan B dapat dikalikan")
    C = (A[0][0]*B[0][0])+(A[0][1]*B[1][0])+(A[0][2]*B[2][0])
    D = (A[0][0]*B[0][1])+(A[0][1]*B[1][1])+(A[0][2]*B[2][1])
    E = (A[0][0]*B[0][2])+(A[0][1]*B[0][0])+(A[0][2]*B[2][2])
    print (C,D,E)
    F = (A[1][0]*B[0][0])+(A[1][1]*B[1][0])+(A[1][0]*B[1][1])
    G = (A[1][0]*B[0][1])+(A[1][1]*B[1][1])+(A[1][2]*B[2][1])
    H = (A[1][0]*B[0][2])+(A[1][1]*B[1][2])+(A[1][2]*B[2][2])
    print (F,G,H)
    I = (A[2][0]*B[0][0])+(A[2][1]*B[1][0])+(A[2][2]*B[2][0])
    J = (A[2][0]*B[0][1])+(A[2][1]*B[1][1])+(A[2][2]*B[2][1])
    K = (A[2][0]*B[0][2])+(A[2][1]*B[1][2])+(A[2][2]*B[2][2])
    print (I,J,K)
