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

int main(int argc, char *argv[])
{

    Country c;

    strcpy(c.name, argv[1]);
    strcpy(c.cap, argv[2]);
    c.pop = atof(argv[3]);
    c.size = atoi(argv[4]);

    printf("%s\n%s\n%.2f million people\n%d km2\n", c.name, c.cap, c.pop, c.size);
    return 0;

}
