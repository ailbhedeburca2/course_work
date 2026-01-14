/*
Author: Ailbhe de Burca
Date: 10/12/25
Description: this program will take a list of integers from command line
and decode it. it does this by counting every repeating consecutive
number and outputting the digit along with that count.
Approach: I am going to make a struct to hold the lists of numbers.
i am hen going to iterate over each list individually and then each
element within that list so i can count how the number of times the
number shows up.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Lists Lists;

struct Lists
{
    char nums[50];
};

void output(Lists *list, int len);

int main(int argc, char *argv[])
{
    int len = argc - 1;
    Lists *list = calloc(len, sizeof(int) * 50);

    for (int i = 0; i < len; i++)
    {
        strcpy(list[i].nums, argv[i + 1]);
    }

    output(list, len);

    free(list);
    list = NULL;

    return 0;
}

void output(Lists *list, int len)
{
    for (int i = 0; i < len; i++)
    {
        int str_len = strlen(list[i].nums);
        if (str_len > 1)
        {
            int index = 0;
            int word_index = 0;
            for (int k = 0; k < str_len;)
            {
                int number = list[i].nums[index];
                int count = 0;
                int j = 0;
                while ((j < str_len) && (number == list[i].nums[index]))
                {
                    count++;
                    index++;
                }
                printf("%c %d", number, count);
                k += count;
                if (k < str_len)
                {
                    printf(" ");
                }
            }
            printf("\n");
        }
        else
        {
            printf("%s 1\n", list[i].nums);
        }
    }
}

