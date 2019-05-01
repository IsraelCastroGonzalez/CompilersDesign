#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char*argv[]){

    char* filename = argv[1];
    FILE* file;
    file = fopen(filename, "r");
    bool isFloat = false;
    
    if (file == NULL) {
        printf("null file");
        return 0;
    }

        char c;
        while ((c = fgetc(file)) != EOF){
            if(c == '\n'){
                printf("\n");
                continue;
            }
            if(c == ' ' || c == '\0'){
                continue;
            }

            if(isdigit(c)){
                while(c!=' ' && c!= '\n'){
                    if(c == '.'){
                        isFloat = true;
                    }
                    c = fgetc(file);
                }
                
                if(isFloat){
                    printf("fNum ");

                }
                else{
                    printf("iNum ");
                }
            }

            switch (c)
            {
                case '\n':
                    printf("\n");
                    break;
                case 'i':
                    printf("IntDcl ");
                    break;
                case 'f':
                    printf("FloatDcl ");
                    break;
                case 'p':
                    printf("PrintDcl ");
                    break;
                case '=':
                    printf("Assign ");
                    break;
                case '+':
                    printf("Addition ");
                    break;
                case '-':
                    printf("Substraction ");
                    break;
                case '*':
                    printf("Multiplication ");
                    break;
                case '/':
                    if(c = fgetc(file) == '/'){
                        printf("Comment ");
                        while(c !='\n'){
                            c = fgetc(file);
                            continue;
                        }
                        printf("\n");
                    }
                    else{
                        printf("Division ");
                        ungetc(c,file);
                    }
                    break;

                default:
                    printf("Id ");
                    break;
            }
    }
    fclose(file);
    printf("\nFinished reading file.\n");
    return 0;
}