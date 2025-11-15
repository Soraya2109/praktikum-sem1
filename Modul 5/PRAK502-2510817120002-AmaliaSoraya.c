#include <stdio.h>
#include <math.h>

int hitung(int nilai1, int nilai2) {
    return abs(nilai1 - nilai2);
}

int mutlak(int nilai1) {
    return abs(nilai1);
}

int main() {
    int a, b, c, d, hasil;

    scanf("%d", &a);
    scanf("%d", &c);
    scanf("%d", &b);
    scanf("%d", &d);

    hasil = hitung(a,b) + hitung(c,d);
    printf("%d", mutlak(hasil));

    return 0;
}