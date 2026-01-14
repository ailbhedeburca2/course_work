/*Write a program ex1-inventory-value.c[✓] that calculates the total value of all products in stock, accounting for discounts. Display the result with two decimal places.

Discount Rules:

The total value of each product in stock is calculated as price * stock.

If a product is marked as "discounted," a discount rate of 10% is applied to the total value of that product.*/


/*Ailbhe de Burca, Inventory Value, 30/10/25)*/
/*I am going to create a structure to hold all the values like before but
this time i will create a function to get the total value of all the stock.
i will do this by multiplying the price by 0.9 if it is discounted and
then multiplying that number by the number of items or if not discounted just
multiplying the price by the number of items*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Inventory Inventory;

/* initializing structure */
struct Inventory
{
    char name[20];
    unsigned int items;
    float price;
    int discount;
};

float total_value(Inventory inv[], float total, int length)
{
    for (int i = 0; i < length; i++)
    {
        if (inv[i].discount == 0)
        {
            /*getting values for non discounted items*/
            total += inv[i].price * inv[i].items;
        }
        else
        {
            /* getting values for discounted items*/
            total += (inv[i].price * 0.9) * inv[i].items;
        }
    }
    return total;
}

int main(int argc, char *argv[])
{

    int length = (argc - 1) / 4;
    Inventory inv[length];

    int index = 1;
    /* setting all values to the structre */
    for (int i = 0; i < length; i++)
    {
        strcpy(inv[i].name, argv[index]);
        inv[i].items = atoi(argv[index + 1]);
        inv[i].price = atof(argv[index + 2]);
        inv[i].discount = atoi(argv[index + 3]);

        index += 4;
    }

    float total = 0;
    float res =  total_value(inv, total, length);
    printf("%.2f\n", res);

    return 0;

}
