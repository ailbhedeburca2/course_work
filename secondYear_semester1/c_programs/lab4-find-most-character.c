#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{

    char *ps = argv[1];

    char letter;
    int max = 0;

    for (char *pi = ps; *pi != '\0'; pi++)
    {
        int count = -1;

        for (char *pj = ps; *pj != '\0'; pj++)
        {
            if (*pi == *pj && *pi != ' ')
            {
                count++;
            }
        }

        if (count > max)
        {
            max = count;
            letter = *pi;
        }
    }

    printf("%c\n", letter);
    return 0;

}
