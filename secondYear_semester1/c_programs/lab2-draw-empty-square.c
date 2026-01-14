#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{

    int width = atoi(argv[1]);
    char star = '*';

    /* TOP */
    for (int i = 0; i < width; i++)
    {
        printf("%c", star);
    }

    printf("\n");

    /* MIDDLE */
    for (int i = 0; i < width - 2; i++)
    {
        for (int j = 0; j < width; j ++)
        {
            if ((j == 0) || (j == width - 1))
            {
                printf("%c", star);
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }

    /* BOTTOM */
    for (int i = 0; i < width; i++)
    {
        printf("%c", star);
    }

    printf("\n");

    return 0;

}
