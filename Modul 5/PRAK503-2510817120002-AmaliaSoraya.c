#include <stdio.h>

int maksimal(int a, int b) {
    int maks = (a > b) ? a : b;
    return maks;
}
int minimal(int a, int b) {
    int minim = (a < b) ? a : b;
    return minim;
}

int main() {
    int batas = 0;
    int maks = -100000;
    int minim = 100000;
    int bilangan;
    scanf("%d", &bilangan);

    while (batas < bilangan) {
        int nilai;
        scanf("%d", &nilai);
        maks = maksimal(maks, nilai);
        minim = minimal(minim, nilai);
        batas ++;
    }
    printf("%d %d", maks, minim);
    return 0;
}