#include <stdio.h>
#include <stdlib.h>

int find_val(int length, int target, int count, int *pNums)
{
    for (int *p = pNums; p != pNums + length; p++)
    {
        if (*p == target)
        {
            return count;
            break;
        }
        count++;
    }
}

int main(int argc, char *argv[])
{

    int length = argc - 2;
    int *pNums = calloc(length, sizeof(int));
    //int output[length];

    int target = atoi(argv[1]);
    int count = 0;

    int index = 2;
    for (int i = 0; i < length; i++)
    {
        pNums[i] = atoi(argv[index]);
        //printf("%d\n", pNums[i]);
        index++;
    }

    int res = find_val(length, target, count, pNums);
    //for (int *p = pOutput; p != pOutput + 
    printf("Found %d at %d\n", target, res);
    return 0;

}
