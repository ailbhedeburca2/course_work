#include <stdio.h>
#include <stdlib.h>

typedef struct List List;

struct List
{
    int num;
    List *next;
};

void output(List *nums);

int main(int argc, char *argv[])
{

    int n = atoi(argv[1]);
    List *nums = calloc(1, sizeof(List));
    List *start = nums;
    int index = 2;
    for (int i = 0; i < n; i++)
    {
        nums->num = atoi(argv[index]);
        index++;

        nums->next = calloc(1, sizeof(List));
        nums = nums->next;
    }

    nums->next = NULL;
    output(start);
    return 0;
}

void output(List *nums)
{
    for (List *p = nums; p->next != NULL; p = p->next)
    {
        printf("%d\n", p->num);
    }
}

