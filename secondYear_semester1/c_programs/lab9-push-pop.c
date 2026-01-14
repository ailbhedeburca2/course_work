#include <stdio.h>
#include <stdlib.h>

typedef struct List List;

struct List
{
    int num;
    List *next;
};

void pop(List *head, int new_int1, int new_int2);

int main(int argc, char *argv[])
{
    int len = atoi(argv[1]);
    int new_int2 = atoi(argv[argc - 1]);
    int new_int1 = atoi(argv[argc - 2]);

    List *curr = calloc(1, sizeof(List));
    List *head = curr;

    int index = 2;
    for (int i = 0; i < len; i++)
    {
        curr->num = atoi(argv[index]);
        index++;
        //printf("%d\n", curr->num);
        curr->next = calloc(1, sizeof(List));
        curr = curr->next;
    }

    curr->next = NULL;
    //printf("%d\n", head->num);
    pop(head, new_int1, new_int2);

    for (List *p = head; p->next != NULL; p = p->next)
    {
        printf("%d\n", p->num);
    }
    return 0;

}

void pop(List *head, int new_int1, int new_int2)
{
    List *p = head;
    while (p->next->next->next->next != NULL)
    {
        p = p->next;
    }

    //printf("%d\n", p->num);
    //p->next = calloc(1, sizeof(List));
    //p = p->next;
    p->next->num = new_int1;

    //p->next->next = calloc(1, sizeof(List));
    //p = p->next;
    p->next->next->num = new_int2;

    p->next->next->next->next = NULL;
}
