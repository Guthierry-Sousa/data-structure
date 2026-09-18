#include <stdio.h>

int main(){

    int arr[10]; //Declarando um array de inteiros de 10 posições

    for(int i = 0; i < 10; i++){
        printf("Informe um  valor para a posição %d: ", i);
        scanf("%d", &arr[i]);
    }

    for(int i = 0; i < 10; i++){
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    return 0;
}