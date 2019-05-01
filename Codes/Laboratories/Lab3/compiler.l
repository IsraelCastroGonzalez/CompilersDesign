%{
#include <stdio.h>
%}

%%
i                       printf("IntDcl");
f                       printf("FloatDcl");
p                       printf("PrintDcl");
[a-eghj-oq-z]           printf("Id");
[0-9]+                  printf("iNum");
[0-9]+"."[0-9]+         printf("fNum");
"="                     printf("Assignment");
"+"                     printf("Addition");
"-"                     printf("Substraction");
"*"                     printf("Multiplication");
"/"                     printf("Division");
"//".*\n                printf("Comment \n");
%%

int main(int argc, char **argv) {
    FILE    *fd;

    if (argc == 2)
    {
        if (!(fd = fopen(argv[1], "r")))
        {
            perror("Error: ");
            return (-1);
        }
        yyset_in(fd);
        yylex();
        fclose(fd);
    }
    else
        printf("Usage: a.out filename\n");
    return (0);
}