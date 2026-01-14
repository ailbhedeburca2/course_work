#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float sum(float, float);
float min(float, float);
float prod(float, float);
float divide(float, float);
float power(float, float);
float nat_log(float, float);
float any_func(float(*pf)(float, float), float a, float b);

int main(int argc, char *argv[])
{

    float a = atof(argv[1]);
    float b = atof(argv[2]);
    float (*pf)(float, float) = NULL;

    pf = sum;
    float res1 = any_func(pf, a, b);
    printf("%.2f\n", res1);

    pf = min;
    float res2 = any_func(pf, a, b);
    printf("%.2f\n", res2);

    pf = prod;
    float res3 = any_func(pf, a, b);
    printf("%.2f\n", res3);

    pf = divide;
    float res4 = any_func(pf, a, b);
    printf("%.2f\n", res4);

    pf = power;
    float res5 = any_func(pf, a, b);
    printf("%.2f\n", res5);

    pf = nat_log;
    float res6 = any_func(pf, a, b);
    printf("%.2f\n", res6);

    return 0;

}

float any_func(float(*pf)(float, float), float a, float b)
{
    return pf(a, b);
}

float sum(float a, float b)
{
    return a + b;
}

float min(float a, float b)
{
    return a - b;
}

float prod(float a, float b)
{
    return a * b;
}

float divide(float a, float b)
{
    return a / b;
}

float power(float a, float b)
{
    return pow(a, b);
}

float nat_log(float a, float b)
{
    return log(a) + log(b);
}
