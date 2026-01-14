#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    char name[50];
    float size;
} City;

typedef struct
{
    char name[50];
    City cities[3];
} Country;

int main(int argc, char *argv[])
{

    int length = (argc - 1) / 7;
    Country c[length];

    int index = 1;
    for (int i = 0; i < length; i++)
    {
        strcpy(c[i].name, argv[index]);

        strcpy(c[i].cities[0].name, argv[index + 1]);
        c[i].cities[0].size = atof(argv[index + 2]);
        strcpy(c[i].cities[1].name, argv[index + 3]);
        c[i].cities[1].size = atof(argv[index + 4]);
        strcpy(c[i].cities[2].name, argv[index + 5]);
        c[i].cities[2].size = atof(argv[index + 6]);

        //printf("%s, %s, %s, %s\n", c[i].name, c[i].cities[0].name, c[i].cities[1].name, c[i].cities[2].name);
        index += 7;
    }

    for (int i = 0; i < length; i++)
    {
        int max = 0;
        char *name = malloc(50);
        for (int j = 0; j < 3; j++)
        {
            if (c[i].cities[j].size > max)
            {
                max = c[i].cities[j].size;
                name = c[i].cities[j].name;
            }
        }
        printf("%s: %s\n", c[i].name, name);
    }
    return 0;

}
