#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int convert(int *nums, int len);

int main(int argc, char *argv[])
{

    int len = argc - 1;

    if (len > 8)
    {
        printf("Too many binary digits entered.\n");
        exit(0);
    }

    int *nums = calloc(len, sizeof(int));

    for (int i = 0; i < len; i++)
    {
        if ((strcmp(argv[i + 1], "1") != 0) && (strcmp(argv[i + 1], "0") != 0))
        {
            printf("Only digits 1 and 0 are permitted.\n");
            exit(0);
        }
        nums[i] = atoi(argv[i + 1]);
    }

    int res = convert(nums, len);
    printf("%d\n", res);

    free(nums);
    nums = NULL;
    return 0;
}

int convert(int *nums, int len)
{
    int power;
    int total = 0;
    for (int i = 0; i < len; i++)
    {
        power = len - 1 - i;
        int pow = 1;
        for (int j = 0; j < power; j++)
        {
            pow *= 2;
        }
        total += pow * nums[i];
    }
    return total;
}
