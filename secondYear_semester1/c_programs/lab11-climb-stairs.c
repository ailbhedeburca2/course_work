#include <stdio.h>
#include <stdlib.h>

int fib(int n);

int main(int argc, char *argv[])
{

    int n = atoi(argv[1]);

    int res = fib(n);
    printf("%d\n", res);

    return 0;
}

int fib(int n)
{
    if (n <= 3)
    {
        return n;
    }

    int total = 0;
    int prev = 0;
    int curr = 1;
    for (int i = 0; i < n; i++)
    {
        total = prev + curr;
        prev = curr;
        curr = total;
    }
    return total;
}
