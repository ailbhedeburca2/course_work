#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{

    int list[10];

    for (int i = 1; i < argc; i++)
    {
        list[i - 1] = atoi(argv[i]);
    }

    int count = 0;
    for (int i = 0; i < argc - 1; i++)
    {
        if (list[i] % 2 != 0)
        {
            count++;
        }
    }

    printf("%d\n", count);

    return 0;
}
