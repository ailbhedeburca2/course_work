#include <stdio.h>
#include <stdlib.h>

int largest_num(int *list, int len)
{
    int max = 0;
    for (int i = 0; i < len; i++)
    {
        if (list[i] > max)
        {
            max = list[i];
        }
    }

    for (int i = 0; i < len; i++)
    {
        if (max / 2 == list[i])
        {
            return max;
            break;
        }
    }
    return 0;

}

int main(int argc, char *argv[])
{

    int len = argc - 1;
    int *list = calloc(len, sizeof(int));

    for (int i = 0; i < len; i++)
    {
        list[i] = atoi(argv[i + 1]);
    }

    int res = largest_num(list, len);
    printf("%d\n", res);

    free(list);
    list = NULL;

    return 0;

}
