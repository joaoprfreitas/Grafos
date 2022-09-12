/*
 * Nome: João Pedro Rodrigues Freitas
 * N USP: 11316552
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int **erdosRenyi(int, double);

void printMatrix(int **, int);
void freeMatrix(int **, int);

int main() {
    int n_vert;
    double p_prob;

    srand(time(NULL)); // Criar sempre números aleatórios

    printf("Digite o número de vértices: ");
    scanf("%d", &n_vert);

    do {
        printf("Digite o valor da constante p (0 < p <= 1): ");
        scanf("%lf", &p_prob);
    } while (p_prob < 0 || p_prob > 1);

    int **matrix = erdosRenyi(n_vert, p_prob);

    printMatrix(matrix, n_vert);

    freeMatrix(matrix, n_vert);

    return EXIT_SUCCESS;
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
            randomValue = (double) rand() / (RAND_MAX + 1.0);

            // Basta preencher com 1 quando satisfizer a condição
            if (randomValue >= p) {
                matrix[i][j] = 1;
                matrix[j][i] = 1;
            }
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