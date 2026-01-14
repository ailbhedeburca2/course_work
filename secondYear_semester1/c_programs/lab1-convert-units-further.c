#include <stdio.h>
#include <stdlib.h>

int main()
{

//    int cm;
//    scanf("%d", &cm);

    float divisor = 2.54;
    int i = 30;

    while(i < 50)
    {

        float inches = i / divisor;
        printf("%7.2f", inches);

        i++;

        if (i % 5 == 0)
        {
            printf("\n");
        }


    }


    return
}
