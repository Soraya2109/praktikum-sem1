#include <stdio.h>

int main() {
    int nilai;
    scanf("%d", &nilai);

    if (nilai >= 80) {
        printf("A");
    } else if (nilai >= 70 && nilai < 80) {
        printf("B");
    } else if (nilai >= 60 && nilai < 70) {
        printf("C");
    } else if (nilai >= 50 && nilai < 60) {
        printf("D");
    } else {
        printf("E");
    }
}