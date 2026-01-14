#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{

    char *pstr = argv[1];
    char *pword = argv[2];

    int counti = 0;
    int end;
    for (char *p = pstr; *p != '\0'; p++)
    {
        counti++;
        if (*p == *pword)
        {
            int countj = counti - 1;
            while ((*p != '\0') && (*pword != '\0') && (*p == *pword))
            {
                pword++;
                p++;
                countj++;
            }
            end = countj;
            break;
        }
    }

    printf("%d %d\n", counti - 1, end - 1);
    return 0;

}
