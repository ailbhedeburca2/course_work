#include <stdio.h>
#include <stdlib.h>

typedef struct List List;

struct List
{
    int num;
    List *next;
};

void insert(List *head, int find, List *pput);

int main(int argc, char *argv[])
{

    int list[10] = {8, 7, 3, 4, 5, 6, 9, 2, 14, 12};
    int len = 10;

    int find = atoi(argv[1]);

    int put = atoi(argv[2]);
    List *pput = calloc(1, sizeof(List));
    pput->num = put;

    List *curr = calloc(1, sizeof(list));
    List *head = curr;

    for (int i = 0; i < len; i++)
    {
        curr->num = list[i];
        //printf("%d\n", curr->num);
        curr->next = calloc(1, sizeof(List));
        curr = curr->next;
    }

    curr->next = NULL;

    insert(head, find, pput);

    for (List *p = head; p->next != NULL; p = p->next)
    {
        printf("%d\n", p->num);
    }
    return 0;

}

void insert(List *head, int find, List *pput)
{
    List *p = head;
    while ((p->next != NULL) && (p->num != find))
    {
        p = p->next;
    }

    List *val = p->next;
    //List *n = p->next->next;
    p->next = pput;
    p->next->next = val;;
}
