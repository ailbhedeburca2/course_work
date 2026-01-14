#include <stdio.h>
#include <stdlib.h>

int find_max(int length, int max, int *nums)
{
    for (int *p = nums; p < nums + length; p++)
    {
        if (*p > max)
        {
            max = *p;
        }
    }
    return max;
}

int main(int argc, char *argv[])
{

    int length = argc - 1;
    int *nums = calloc(length, sizeof(int));
    int max = 0;
    for (int i = 0; i < length; i++)
    {
        nums[i] = atoi(argv[i + 1]);
    }

    int res = find_max(length, max, nums);
    printf("%d\n", res);

    return 0;

}
