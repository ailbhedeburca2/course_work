#include <stdio.h>
#include <stdlib.h>

int isLeapYear(int year)
{
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

void printLeapYears(int start, int end)
{
    for (int year = start; year <= end; year++)
    {
        if (isLeapYear(year))
        {
            printf("%d\n", year);
        }
    }
}

int main(int argc, char*argv[])
{

    int start = atoi(argv[1]);
    int end = atoi(argv[2]);

    if (start < 1582) start = 1582;
    if (end > 2020) end = 2020;

    printLeapYears(start, end);

    return 0;

}
