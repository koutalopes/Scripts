#include <stdio.h>

int main() {
    int vSaque, nota20, nota50;

    printf("Valor do saque: ");
    scanf("%d", &vSaque);

    if (vSaque > 500) {
        printf("Valor acima.\n");
    } else if ((vSaque % 10) != 0 || ((vSaque < 40) && (vSaque % 20) != 0)) {
        printf("Valor inválido.\n");
    } else {
        if (((vSaque % 50) % 20) == 0) {
            nota50 = vSaque / 50;
            nota20 = (vSaque % 50) / 20;
        } else if ((vSaque % 20) != 0) {
            nota50 = (vSaque / 50) - 1;
            nota20 = ((vSaque % 50) + 50) / 20;
        }
        printf("Notas de 20: %d\n", nota20);
        printf("NOtas de 50: %d\n", nota50);
    }

    return 0;
}
