#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    char name[50];
    char cap[50];
    float pop;
    int size;
} Country;

void output(Country *c, int length);

int main(int argc, char *argv[])
{

    int length = (argc - 1) / 4;
    Country c[length];

    int index = 1;
    for (int i = 0; i < length; i++)
    {
        strcpy(c[i].name, argv[index]);
        strcpy(c[i].cap, argv[index + 1]);
        c[i].pop = atof(argv[index + 2]);
        c[i].size = atoi(argv[index + 3]);
        index += 4;
    }

    output(c, length);
    return 0;
}

void output(Country *c, int length)
{
    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length; j++)
        {
            if (c[j].pop < c[i].pop)
            {
                Country tmp = c[i];
                c[i] = c[j];
                c[j] = tmp;
            }
        }
    }

    printf("Country\t\t\tCapital\t\t\tSize\t\t\tPopulation\n");
    for (int i = 0; i < length; i++)
    {
        printf("%s\t\t\t%s\t\t\t%d\t\t\t%.2f\n", c[i].name, c[i].cap, c[i].size, c[i].pop);
    }
}
