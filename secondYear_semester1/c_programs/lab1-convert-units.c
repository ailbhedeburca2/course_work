#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{

    int cm = atoi(argv[1]);

    float converter = 2.54;
//    printf("%f\n", converter);
    
    float inches = cm / converter;

    printf("%.2f\n", inches);

    return 0;

}
