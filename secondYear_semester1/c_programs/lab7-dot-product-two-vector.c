#include <stdio.h>
#include <stdlib.h>

int dot_prod(int *vector1, int *vector2, int total, int n);

int main(int argc, char *argv[])
{

    int n = atoi(argv[1]);
    int *vector1 = malloc(n);
    int *vector2 = malloc(n);

    int length = argc - 3;
    int index = 2;
    for (int i = 0; i < n; i++)
    {
        vector1[i] = atoi(argv[index + i]);
        vector2[i] = atoi(argv[index + n + i]);
    }
    int total = 0;
    int res = dot_prod(vector1, vector2, total, n);
    printf("%d\n", res);
    free(vector1);
    free(vector2);
    vector1 = NULL;
    vector2 = NULL;
    return 0;
}

int dot_prod(int *vector1, int *vector2, int total, int n)
{
    for (int i = 0; i < n; i++)
    {
        total += vector1[i] * vector2[i];
    }
    return total;

}

