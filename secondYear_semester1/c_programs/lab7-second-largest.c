#include <stdio.h>
#include <stdlib.h>

void sort_list(float *nums, int length);
float find_second_largest(float *nums, int length);

int main(int argc, char *argv[])
{

    int length = argc - 1;
    float *nums = calloc(length, sizeof(float));

    for (int i = 0; i < length; i++)
    {
        nums[i] = atof(argv[i + 1]);
    }

    sort_list(nums, length);
    float res = find_second_largest(nums, length);
    printf("%.1f\n", res);

    return 0;

}

void sort_list(float *nums, int length)
{
    for (float *p = nums; p < nums + length; p++)
    {
        for (float *pj = p + 1; pj < nums + length; pj++)
        {
            if (*pj < *p)
            {
                float tmp = *p;
                *p = *pj;
                *pj = tmp;
            }
        }
    }
}

float find_second_largest(float *nums, int length)
{
    float max = nums[length - 1];
    float *p = nums;
    while (*p != max)
    {
        p++;
    }

    return *(p - 1);
}
