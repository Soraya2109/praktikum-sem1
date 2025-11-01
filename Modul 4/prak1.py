angka, simbol = input().split()

for perhitungan in range(1, 51) :
    if perhitungan % int(angka) == 0 :
        print(simbol, end=" ")
    else :
        print(perhitungan, end=" ")