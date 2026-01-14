#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{

    int len = argc - 1;

    char **words = malloc(len * sizeof(char *));

    for (int i = 0; i < len; i++)
    {
        words[i] = malloc(strlen(argv[i + 1] + 1));
        strcpy(words[i], argv[i + 1]);
    }

    int max = 0;
    for (char **pi = words; pi < words + len; pi++)
    {
        int count = 0;

        for (char *pj = *pi; *pj != '\0'; pj++)
        {
            count++;
        }
        if (count > max)
        {
            max = count;
        }
    }

    for (char **p = words; p < words + len; p++)
    {
        if (strlen(*p) == max)
        {
            printf("%s\n", *p);
        }
    }

    free(words);
    words = NULL;

    return 0;

}
