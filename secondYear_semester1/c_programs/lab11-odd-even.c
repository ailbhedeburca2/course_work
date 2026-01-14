#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

    int n = atoi(argv[1]);

    //printf("%d\n", n & 1);
    if ((n & 1) == 0)
    {
        printf("Even\n");
    }
    else
    {
        printf("Odd\n");
    }

    return 0;
}
