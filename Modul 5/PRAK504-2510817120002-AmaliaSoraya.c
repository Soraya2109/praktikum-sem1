#include <stdio.h>

int reverse(int nilai) {
    int hasil = 0, sisa;
    while (nilai != 0) {
        sisa = nilai % 10;
        hasil = hasil * 10 + sisa;
        nilai /= 10;
    }
    return hasil;
}

int main() {
    int A, B, C;
    scanf("%d %d",&A,&B);
    A = reverse(A);
    B = reverse(B);
    C = A + B;
    printf("%d",reverse(C));

    return 0;
}