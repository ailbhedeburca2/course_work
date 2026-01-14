#include <stdio.h>
#include <stdlib.h>

typedef struct Customer Customer;

struct Customer
{
    int id;
    Customer *next;
};

void reorder(Customer *head, int *nums);

int main(int argc, char *argv[])
{

    Customer *c = calloc(1, sizeof(Customer));
    Customer *head = c;

    int len = argc - 1;
    for (int i = 0; i < len; i++)
    {
        c->id = atoi(argv[i + 1]);
        c->next = calloc(1, sizeof(Customer));

        c = c->next;
    }

    c->next = NULL;

    int *nums = calloc(len, sizeof(int));
    reorder(head, nums);

    for (int i = 0; i < len; i++)
    {
        printf("%d\n", nums[i]);
    }

    Customer *curr = head;
    while (curr != NULL)
    {
        Customer *next = curr->next;
        free(curr);
        curr = next;
    }
    return 0;
}

void reorder(Customer *head, int *nums)
{
    int index = 0;
    for (Customer *p = head; p->next != NULL; p = p->next)
    {
        if (p->id % 2 == 0)
        {
            nums[index] = p->id;
            index++;
        }
    }

    for (Customer *p = head; p->next != NULL; p = p->next)
    {
        if (p->id % 2 != 0)
        {
            nums[index] = p->id;
            index++;
        }
    }
}
