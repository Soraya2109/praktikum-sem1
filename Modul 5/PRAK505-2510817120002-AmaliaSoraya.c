#include <stdio.h>

void Biodata(int tahunlahir, char nama[], char asal[]){
    int umur, tahun_sekarang = 2025;
    umur = tahun_sekarang - tahunlahir;
    printf("\nPerkenalkan Nama Saya : %s\n", nama);
    printf("Umur Saya : %d\n", umur);
    printf("Saya Adalah Angkatan : %d\n", tahun_sekarang);
    printf("Asal Saya dari : %s", asal);
}

int main() {
    int tahunLahir;
    char Namaku[20], Asal[15];
    scanf(" %d",&tahunLahir);
    scanf(" %[^\n]%*c",&Namaku);
    scanf(" %[^\n]%*c",&Asal);
    Biodata(tahunLahir, Namaku, Asal);
    return 0;
}