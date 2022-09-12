#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "linkedList.h"

#define MAX_RANGE 100

int **erdosRenyi(int, double);
int grau(int **, int, int);
linkedList *listaVertices(int **, int, int);

void printMatrix(int **, int);
void freeMatrix(int **, int);

int main() {
    linkedList *list = NULL;

    int n, vertice;
    double p_prob;

    srand(time(NULL)); // Criar sempre números aleatórios

    printf("Digite o número de vértices: ");
    scanf("%d", &n);

    do {
        printf("Digite o valor da constante p (0 < p <= 1): ");
        scanf("%lf", &p_prob);
    } while (p_prob < 0 || p_prob > 1);

    int **matrix = erdosRenyi(n, p_prob);

    printMatrix(matrix, n);

    printf("Digite o valor de um determinado vértice [0 - N] para mais informações: ");
    scanf("%d", &vertice);

    printf("O grau do vértice %d é %d\n", vertice, grau(matrix, n, vertice));

    list = listaVertices(matrix, n, vertice);
    printf("A lista de adjacência do vértice %d é: ", vertice);
    printList(list);


    

    freeMatrix(matrix, n);
    destroyList(list);

    return EXIT_SUCCESS;
}

int grau(int **matrix, int n, int vertice) {
    int grau = 0;

    for (int i = 0; i < n; i++) {
        if (matrix[vertice][i] == 1) grau++;
    }

    return grau;
}

linkedList *listaVertices(int **matrix, int n, int vertice) {
    linkedList *list = createList();

    for (int i = 0; i < n; i++) {
        if (matrix[vertice][i] == 1) addNode(list, i);
    }

    return list;
}

/*
 * Método de Erdos-Renyi de geração aleatória
 * de grafos não direcionados.
 * 
 * Se randomValue >= p ==> aresta permitida
 * se não, aresta proibida.
 */
int **erdosRenyi(int n, double p) { // n vertices, p probabilidade
    int **matrix = malloc(sizeof(int *) * n);

    // Cria uma matriz preenchida com 0
    for (int i = 0; i < n; i++)
        matrix[i] = calloc(n, sizeof(int));

    double randomValue;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {

            // Gera um valor aleatório e normaliza esse valor
            randomValue = (rand() % MAX_RANGE) / (double) MAX_RANGE;

            // Basta preencher com 1 quando satisfizer a condição
            if (randomValue >= p) matrix[i][j] = 1;
            
            matrix[j][i] = matrix[i][j];
        }
    }

    return matrix;
}

/*
 * Realiza a impressão da matriz
 */
void printMatrix(int **matrix, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

/*
 * Destroi a matriz criada
 */
void freeMatrix(int **matrix, int n) {
    for (int i = 0; i < n; i++)
        free(matrix[i]);
    
    free(matrix);
}