ordo = int(input())

def matriks_ordo2() :
    print("Matriks A")
    matriksA = []
    a_a1 = list(map(int, input().split(" ")))
    a_a2 = list(map(int, input().split(" ")))
    matriksA.append(a_a1)
    matriksA.append(a_a2)
    print("Matriks B")
    matriksB = []
    b_a1 = list(map(int, input().split(" ")))
    b_a2 = list(map(int, input().split(" ")))
    matriksB.append(b_a1)
    matriksB.append(b_a2)

    hasil_ordo2 = [[0, 0], [0, 0]]

    for i in range(len(matriksA)) :
        for j in range(len(matriksB[0])) :
            for k in range(len(matriksB)) :
                hasil_ordo2[i][j] += matriksA[i][k] * matriksB[k][j]
    
    print("\n Matriks AXB")
    for i in range(ordo) :
        for j in range(ordo) :
            print(hasil_ordo2[i][j], end=" ")
        print()

def matriks_ordo3() :
    print("Matriks A")
    matriksA = []
    a_a1 = list(map(int, input().split(" ")))
    a_a2 = list(map(int, input().split(" ")))
    a_a3 = list(map(int, input().split(" ")))
    matriksA.append(a_a1)
    matriksA.append(a_a2)
    matriksA.append(a_a3)
    print("Matriks B")
    matriksB = []
    b_a1 = list(map(int, input().split(" ")))
    b_a2 = list(map(int, input().split(" ")))
    b_a3 = list(map(int, input().split(" ")))
    matriksB.append(b_a1)
    matriksB.append(b_a2)
    matriksB.append(b_a3)

    hasil_ordo3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(len(matriksA)) :
        for j in range(len(matriksB[0])) :
            for k in range(len(matriksB)) :
                hasil_ordo3[i][j] += matriksA[i][k] * matriksB[k][j]
    
    print("\n Matriks AXB")
    for i in range(ordo) :
        for j in range(ordo) :
            print(hasil_ordo3[i][j], end=" ")
        print()

if ordo == 2 :
    matriks_ordo2()
elif ordo == 3:
    matriks_ordo3()