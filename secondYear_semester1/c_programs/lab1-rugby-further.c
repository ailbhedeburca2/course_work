#include <stdio.h>
#include <stdlib.h>

int main()
{

    int Try, conversion, penalty, drop_goal;
    scanf("%d\n%d\n%d\n%d", &Try, &conversion, &penalty, &drop_goal);

    if ((Try < 0) || (conversion < 0) || (penalty < 0) || (drop_goal < 0))
    {

        printf("Invalid input\nPlease enter positive values or make sure all values are inputed\n");
        scanf("%d\n%d\n%d\n%d", &Try, &conversion, &penalty, &drop_goal);

    }

    int score = Try * 5 + conversion * 2 + penalty * 3 + drop_goal * 3;


    printf("%d\n", score);

    return 0;

}
