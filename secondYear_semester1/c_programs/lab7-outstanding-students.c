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

float Adverage(int length, Student *pStudent)
{
    float total = 0;
    for (Student *p = pStudent; p < pStudent + length / 3; p++)
    {
        total += p->grade;
    }

    float adverage = total / (length / 3);
    return adverage;
}

int main(int argc, char *argv[])
{

    Student *pStudent = calloc(2, sizeof(Student));

    int length = argc - 1;
    Student *pTemp = NULL;
    if ((length / 3) > 2)
    {
        pTemp = realloc(pStudent, (length / 3) * sizeof(Student));
        if (!pTemp)
        {
            printf("Memory reallocation failed\n");
            free(pStudent);
            pStudent = NULL;
        }
        else
        {
            pStudent = pTemp;
        }
    }

    int index = 1;
    for (int i = 0; i < length / 3; i++)
    {
        strcpy(pStudent[i].name, argv[index]);
        strcpy(pStudent[i].program, argv[index + 1]);
        pStudent[i].grade = atof(argv[index + 2]);

        index += 3;
    }

    //printf("%s\n", pStudent[0].program);
    float res = Adverage(length,  pStudent);
    for (Student *p = pStudent; p < pStudent + length / 3; p++)
    {
        if ((p->grade > res) && (strcmp(p->program, "CSCE") == 0))
        {
            printf("%s, %.2f\n", p->name, p->grade);
        }
    }
    printf("Average grade: %.2f\n", res);
    return 0;

}
