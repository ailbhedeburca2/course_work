#include <stdio.h>
#include <stdlib.h>

/*typedef struct Student Student;

struct Student
{
    char name[50];
    char colleg[50];
    int age;
    float grade;
}*/

int main(int argc, char *argv[])
{

    FILE *pfile = NULL;
    char *filename = "studentBinary.bin";
    pfile = fopen(filename, "r");

    if (!pfile)
    {
        printf("%Failed to open file\n");
    }

    int namelen;
    fread(&namelen, sizeof(int), 1, pfile);

    char *name = malloc(namelen + 1);
    fread(name, sizeof(char), namelen, pfile);
    name[namelen] = '\0';

    int college_namelen;
    fread(&college_namelen, sizeof(int), 1, pfile);

    char *college_name = malloc(college_namelen + 1);
    fread(college_name, sizeof(char), college_namelen, pfile);
    college_name[college_namelen] = '\0';

    int age;
    fread(&age, sizeof(int), 1, pfile);

    float grade;
    fread(&grade, sizeof(int), 1, pfile);

    fclose(pfile);
    pfile = NULL;

    printf("Name: %s\nCollege: %s\nAge: %d\nGrade: %.2f\n", name, college_name, age, grade);
    return 0;
}
