#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{

    FILE *pf = NULL;
    pf = fopen("paragraph.txt", "rb");
    if (!pf)
    {
        printf("ERROR!\n");
        exit(1);
    }

    char line[201];
    char max_line[201];
    int max_len = 0;

    while (fgets(line, sizeof(line), pf) != NULL)
    {
        int len = strlen(line);

        if (len > max_len)
        {
            max_len = len;
            strcpy(max_line, line);
        }
    }

    printf("%d\n%s\n", max_len, max_line);
    return 0;
}
