#include <stdio.h>
#include <stdlib.h>

typedef struct List List;

struct List
{
    float num;
    List *next;
    List *prev;
};

void output(List *head);

int main(int argc, char *argv[])
{

    List *nums = calloc(1, sizeof(List));
    List *head = nums;
    List *prev = NULL;
    head->prev = NULL;

    int n = atoi(argv[1]);

    int index = 2;
    for (int i = 0; i < n; i++)
    {
        nums->num = atof(argv[index]);
        index++;

        nums->next = calloc(1, sizeof(List));
        nums->next->prev = nums;
        nums = nums->next;
    }

    nums->next = NULL;

    output(head);

    return 0;
}

void output(List *head)
{
    while (head->next->next != NULL)
    {
        head = head->next;
    }

    while (head != NULL)
    {
        printf("%.2f\n", head->num);
        head = head->prev;
    }

}
