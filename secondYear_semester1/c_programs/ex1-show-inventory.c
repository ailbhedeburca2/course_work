/*Write a program ex1-show-inventory.c[✓] that takes input in the format described above and displays each product’s details in one line. For the discount information, display "Discounted" if the discount is available, otherwise "No Discount".*/

/*Ailbhe de Burca,Inventory List, 30/10/25*/
/*Approach: I am going to create a structure to hold all the information
and then I will loop through the structure items to print them out
and putting an if statement to deal with printing the discounts*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Inventory Inventory;

struct Inventory
{
    char name[20];
    unsigned int items;
    float price;
    int discount;
};

int main(int argc, char *argv[])
{

    int len = (argc - 1) / 4;
    Inventory inv[len];

    int index = 1;
    /* setting all the values to the structure */
    for (int i = 0; i < len; i++)
    {
        strcpy(inv[i].name, argv[index]);
        inv[i].items = atoi(argv[index + 1]);
        inv[i].price = atof(argv[index + 2]);
        inv[i].discount = atoi(argv[index + 3]);

        index += 4;
    }

    /* loop to print output */
    for (int i = 0; i < len; i++)
    {
        if (inv[i].discount == 0)
        {
            printf("%s,%d,%.2f,No Discount\n", inv[i].name, inv[i].items, inv[i].price);
        }
        else
        {
            printf("%s,%d,%.2f,Discounted\n", inv[i].name, inv[i].items, inv[i].price);
        }
    }
    return 0;

}
