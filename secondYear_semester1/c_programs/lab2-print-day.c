#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char*argv[])
{

    int n = atoi(argv[1]);

    char list[7][10];
    strcpy(list[0], "Sunday");
    strcpy(list[1], "Monday");
    strcpy(list[2], "Tuesday");
    strcpy(list[3], "Wednesday");
    strcpy(list[4], "Thursday");
    strcpy(list[5], "Friday");
    strcpy(list[6], "Saturday");


    for (int i = -1; i < 7; i++)
    {
        //printf("%s\n", list[i]);
        if (i + 1 == n)
        {
            printf("%s\n", list[i]);
        }
    }

    return 0;

}
