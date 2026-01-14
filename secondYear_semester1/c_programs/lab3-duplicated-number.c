#include <stdio.h>
#include <stdlib.h>

int find_dup(int length, int *pNums)
{
    for (int *pi = pNums; pi != pNums + length; pi++)
    {
        for (int *pj = pi + 1; pj != pNums + length; pj++)
        {
            if (*pj == *pi)
            {
                return *pj;
                break;
            }
        }
    }
    return -1;

}

int main(int argc, char *argv[])
{

    int length = argc - 1;
    int *pNums = calloc(length, sizeof(int));

    for (int i = 0; i < length; i++)
    {
        pNums[i] = atoi(argv[i + 1]);
    }

    int res = find_dup(length, pNums);
    if (res == -1)
    {
        printf("no duplicated number\n");
    }
    else
    {
        printf("%d\n", res);
    }

    return 0;

}
