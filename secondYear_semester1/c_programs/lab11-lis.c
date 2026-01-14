#include <stdio.h>
#include <stdlib.h>

int max(int a, int b);

int main(int argc, char *argv[])
{

    int n = argc - 1;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        arr[i] = atoi(argv[i + 1]);
    }

    int dp[n];
    for (int i = 0; i < n; i++)
    {
        dp[i] = 1;
    }

    for (int i = 1; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (arr[i] > arr[j])
            {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    int lis = dp[0];
    for (int i = 0; i < n; i++)
    {
        if (dp[i] > lis) lis = dp[i];
    }

    printf("%d\n", lis);
    return 0;
}

int max (int a, int b)
{
    return (a > b) ? a : b;
}
