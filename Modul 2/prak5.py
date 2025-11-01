waktu = int(input())

detik = waktu % 60
menit = int((waktu / 60) % 60)
jam = int((waktu / 3600) % 24)
hari = int((waktu / 86400)) 

if waktu < 86400 :
    print(f"{jam:02}:{menit:02}:{detik:02}")
elif waktu >= 86400 :
    print(f"{hari} hari {jam:02}:{menit:02}:{detik:02}")