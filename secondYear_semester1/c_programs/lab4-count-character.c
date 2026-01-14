#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int count_char(int count, char *pchar, char *pstr)
{
    for (char *p = pstr; *p != '\0'; p++)
    {
        if (('A' <= *p) && (*p <= 'Z'))
        {
            *p = *p + 32;
        }
        if (*p == *pchar)
        {
            count++;
        }
    }
    return count;
}
int main(int argc, char *argv[])
{

    char *pchar = argv[1];
    if (('A' <= *pchar) && (*pchar <= 'Z'))
    {
        *pchar = *pchar + 32;
    }
    char *pstr = argv[2];
    int count = 0;

    int res = count_char(count, pchar, pstr);
    printf("%d\n", res);

    return 0;

}
