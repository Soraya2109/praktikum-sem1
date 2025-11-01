#include <stdio.h>

int main() {
    int waktu, detik, menit, jam, hari;
    scanf("%d", &waktu);

    detik = waktu % 60;
    menit = (waktu / 60) % 60;
    jam = (waktu / 3600) % 24;
    hari = waktu / 86400;

    if (waktu < 86400) {
        printf("%.2d:%.2d:%.2d", jam, menit, detik);
    } else if (waktu >= 86400) {
        printf("%d hari %.2d:%.2d:%.2d", hari, jam, menit, detik);
    }
}