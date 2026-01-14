#include <stdio.h>
#include <stdlib.h>
#include <string.h>

float mul(float a, float b)
{
    return a * b;
}

float divide(float a, float b)
{
    return a / b;
}

int main(int argc, char *argv[])
{

    float a = atof(argv[2]);
    float b = atof(argv[3]);


    if (strcmp(argv[1], "multiply") == 0)
    {
        float res = mul(a, b);
        printf("%f\n", res);
    }
    else if (strcmp(argv[1], "divide") == 0)
    {
        if (b != 0)
        {
            float res = divide(a, b);
            printf("%f\n", res);
        }
        else
        {
            printf("invalid\n");
        }
    }
    else
    {
        printf("Invalid input\n");
    }

    return 0;

}

