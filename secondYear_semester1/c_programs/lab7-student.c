#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Student Student;

struct Student
{
    char name[20];
    char program[20];
    float grade;
};

int main(int argc, char *argv[])
{

    Student *pStudent = calloc(2, sizeof(Student));

    int length = argc - 1;
    Student *pTemp = NULL;

    if ((length / 3) > 2)
    {
        pTemp = realloc(pStudent, length * sizeof(Student));
        if (!pTemp)
        {
            printf("Memory reallocation failed\n");
            free(pStudent);
            pStudent = NULL;
            return 0;
        }
        else
        {
            pStudent = pTemp;
        }
    }

    int index = 1;
    for (int i = 0; i < (length / 3); i++)
    {
        strcpy(pStudent[i].name, argv[index]);
        strcpy(pStudent[i].program, argv[index + 1]);
        pStudent[i].grade = atof(argv[index + 2]);

        index += 3;
    }

    for (Student *p = pStudent; p < pStudent + (length / 3); p++)
    {
        printf("%s, %s, %.2f\n", (*p).name, (*p).program, (*p).grade);
    }

    return 0;
}

