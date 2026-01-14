#include <stdio.h>
#include <stdlib.h>

int* sort(int length, int *pNums)
{
    for (int *pi = pNums; pi != pNums + length; pi++)
    {
        for (int *pj = pNums; pj != pNums + length; pj++)
        {
            if (*pi < *pj)
            {
                int tmp = *pi;
                *pi = *pj;
                *pj = tmp;
            }
        }
    }

    return pNums;

}

int main(int argc, char *argv[])
{

    int length = argc - 1;
    int *pNums = calloc(length, sizeof(int));
    for (int i = 0; i < length; i++)
    {
        pNums[i] = atoi(argv[i + 1]);
    }

    int *res = sort(length, pNums);
    for (int i = 0; i < length; i++)
    {
        printf("%d\n", res[i]);
    }

    return 0;

}
