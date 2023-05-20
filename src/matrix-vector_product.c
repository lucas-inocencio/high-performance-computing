#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
    double value1;
    double value2;
} DoublePair;

double** createMatrix(int N) {
    double** matrix = (double**)malloc(N * sizeof(double*));
    for (int i = 0; i < N; i++) {
        matrix[i] = (double*)malloc(N * sizeof(double));
    }
    return matrix;
}

double* createVector(int N) {
    return (double*)malloc(N * sizeof(double));
}

void initializeMatrix(double** matrix, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            matrix[i][j] = (double)rand() / RAND_MAX;
        }
    }
}

void initializeVector(double* vector, int N) {
    for (int i = 0; i < N; i++) {
        vector[i] = (double)rand() / RAND_MAX;
    }
}

DoublePair computeMatrixVectorProduct(double** matrix, double* vector, double* result, int N, FILE* file) {
    DoublePair pair;
    clock_t start, end;
    double cpu_time_used_ij, cpu_time_used_ji;

    start = clock();

    for (int i = 0; i < N; i++) {
        result[i] = 0.0;
        for (int j = 0; j < N; j++) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    end = clock();
    pair.value1 = ((double)(end - start)) / CLOCKS_PER_SEC;

    start = clock();

    for (int i = 0; i < N; i++) {
        result[i] = 0.0;
    }

    for (int j = 0; j < N; j++) {
        for (int i = 0; i < N; i++) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    end = clock();
    pair.value2 = ((double)(end - start)) / CLOCKS_PER_SEC;

    return pair;
}

void freeMatrix(double** matrix, int N) {
    for (int i = 0; i < N; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

void freeVector(double* vector) {
    free(vector);
}

int main() {
    int N;
    int N_list[] = {1, 10, 100, 1000, 10000, 15000, 20000, 25000};

    srand(time(NULL));

    FILE* file = fopen("results.csv", "w");

    for (int len_list = 0; len_list < 80; len_list++) {
        DoublePair pair;
        N = N_list[len_list % 8];

        double** A = createMatrix(N);
        double* x = createVector(N);
        double* B = createVector(N);

        initializeMatrix(A, N);
        initializeVector(x, N);

        // Compute matrix-vector product and write on file
        pair = computeMatrixVectorProduct(A, x, B, N, file);

        fprintf(file, "%d, %f, %f\n", N, pair.value1, pair.value2);

        freeMatrix(A, N);
        freeVector(x);
        freeVector(B);
    }

    fclose(file);

    return 0;
}