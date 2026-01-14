#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void asc(int*, int);
void desc(int*, int);
void any_func(void(*pf)(int*, int), int *nums, int length);

int main(int argc, char *argv[])
{

    int length = atoi(argv[1]);;
    int *nums = calloc(length, sizeof(int));

    int index = 2;
    for (int i = 0; i < length; i++)
    {
        nums[i] = atoi(argv[index + i]);
        //printf("%d\n", nums[i]);
    }

    void (*pf)(int*) = NULL;

    if (strcmp(argv[argc - 1], "asc"))
    {
        any_func(asc, nums, length);
    }
    else
    {
        any_func(desc, nums, length);
    }

    printf("Sorted numbers:");
    for (int i = 0; i < length; i++)
    {
        printf(" %d", nums[i]);
    }
    printf("\n");
    return 0;

}

void any_func(void(*pf)(int*, int), int *nums, int length)
{
    return pf(nums, length);
}

void asc(int *nums, int length)
{
    for (int *p = nums; p < nums + length; p++)
    {
        for (int *pj = p + 1; pj < nums + length; pj++)
        {
            if (*pj > *p)
            {
                int tmp = *p;
                *p = *pj;
                *pj = tmp;
            }
        }
    }
}

void desc(int *nums, int length)
{
    for (int *p = nums; p < nums + length; p++)
    {
        for (int *pj = p + 1; pj < nums + length; pj++)
        {
            if (*pj < *p)
            {
                int tmp = *p;
                *p = *pj;
                *pj = tmp;
            }
        }
    }
}
