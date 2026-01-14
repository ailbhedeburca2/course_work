#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

    int n = atoi(argv[1]);
    int *pNums = calloc(n * n, sizeof(int));

    int index = 2;
    for (int i = 0; i < n * n; i++)
    {
        pNums[i] = atoi(argv[index]);
        index ++;
    }


    int total = 0;
    for (int i = 0; i < n; i++)
    {
        int j = i;
        //printf("%d\n", pNums[i * n + j]);
        total += pNums[i * n + j];
    //    printf("%d\n", total);
    }


    printf("%d\n", total);
    return 0;

}
