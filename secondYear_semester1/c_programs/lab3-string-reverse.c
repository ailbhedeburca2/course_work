#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* reverse(int length, char string[50], char New_str[50])
{
    for (int i = 0; i < length; i++)
    {
        New_str[i] = string[length - 1 - i];
    }
    New_str[length] = '\0';
    return New_str;
}

int main(int argc, char *argv[])
{

    char string[50];
    strcpy(string, argv[1]);
    char New_str[50];

    int length = strlen(argv[1]);

    char* res = reverse(length, string, New_str);
    printf("%s\n", res);

    return 0;

}
