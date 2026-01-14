/*The maximum difference between elements in an array is the highest difference obtained by subtracting one element from another within the array.

Write a program ex1-max-diff.c[✓] that accepts input as an array of integers. Given the number of elements in the array (between 2 and 100), the program finds and displays the maximum difference between any two elements in the array.

Constraints:

The maximum number of elements in the array is 100.

The array will have at least two elements.*/


/*Ailbhe de Burca, Maximum Difference Finder, 30/10/25*/
/*Approach: I am going to find the largest digit in the array and then minus
the smallest digit in the array to find the largest difference*/
#include <stdio.h>
#include <stdlib.h>

int find_largest(int *nums, int len, int max)
{
    for (int i = 0; i < len; i++)
    {
        if (nums[i] > max)
        {
            max = nums[i];
        }
    }
    return max;
}

int find_smallest(int *nums, int len, int min)
{
    for (int i = 0; i < len; i++)
    {
        if (nums[i] < min)
        {
            min = nums[i];
        }
    }
    return min;
}
int main(int argc, char *argv[])
{

    int len = argc - 1;
    int nums[len];

    for (int i = 0; i < len; i++)
    {
        nums[i] = atoi(argv[i + 1]);
    }

    int max = nums[0];
    int big = find_largest(nums, len, max); //getting largest value in array

    int min = nums[0];
    int small = find_smallest(nums, len, min); //getting smallest value in array

    printf("%d\n", big - small); // getting the largest diffenerence in array

    return 0;

}
