#include <stdio.h>

int maxBilangan(int nilai1, int nilai2, int nilai3, int nilai4) {
    int maks1, maks2, maks;
    maks1 = (nilai1 > nilai2) ? nilai1 : nilai2;
    maks2 = (nilai3 > nilai4) ? nilai3 : nilai4;
    maks = (maks1 > maks2) ? maks1 : maks2;
    return maks;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int hasil = maxBilangan(a, b, c, d);
    printf("%d", hasil);

    return 0;
}