angka = int(input())

if angka == 0 :
    print("Nol")
elif 1 <= angka < 10 :
    print("Satuan")
elif 10 < angka < 20 :
    print("Belasan")
elif angka == 10 or 20 <= angka < 100 :
    print("Puluhan")
else :
    print("Anda Menginput Melebihi Limit Bilangan")