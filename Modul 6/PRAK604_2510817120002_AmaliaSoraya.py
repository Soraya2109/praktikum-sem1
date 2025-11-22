pesan1 = input()
pesan2 = input()

def identifikasi():
    list1 = []
    list2 = []

    for msg1 in pesan1 :
        list1.append(msg1)

    for msg2 in pesan2 :
        list2.append(msg2)

    nomor = 0
    simbolis = []

    for samain in range(len(pesan1)) :
        if list1[nomor] == list2[nomor] and list2[nomor] == " " :
            simbolis.append(" ")
        elif list1[nomor] == list2[nomor] :
            simbolis.append("*")
        elif list1[nomor] != list2[nomor] :
            simbolis.append("#")
        nomor += 1

    for hasil in simbolis :
        print(hasil, end="")

    count_bintang = 0
    count_tagar = 0

    for simbol in simbolis :
        if simbol == "*" :
            count_bintang += 1

        elif simbol == "#" :
            count_tagar += 1

    print()
    print(f"* = {count_bintang}")
    print(f"# = {count_tagar}")

    print(f"Pesan asli" if count_bintang >= count_tagar else "Pesan palsu")

if len(pesan1) != len(pesan2) :
    print("Panjang kalimat berbeda, pesan palsu")

else :
    identifikasi()