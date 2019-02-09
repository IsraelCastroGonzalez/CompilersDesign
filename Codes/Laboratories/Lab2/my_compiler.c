#include <stdio.h>
typedef int bool;
#define true 1
#define false 0

int main(){
    int c;
    int parenthesisCount;
    int bracketsCount;
    int quotesCount;
    bool open;

    FILE *file;
    file = fopen("hello.c", "r");
    if (file) {
        while ((c = getc(file)) != EOF)
            if(c == '{'){
                bracketsCount++;
            }
            if(c == '}'){
                bracketsCount--;
            }
            if(c == '"' && open){
                bracketsCount++;
                open = false;
            }
            if(c == '"'){
                bracketsCount--;
                open = true;
            }      
            putchar(c);
        fclose(file);
    }
    if(parenthesisCount < 0){
        printf("Error, te falta parentesis de apertura.\n");
    }else if (parenthesisCount > 0){
        printf("Error, te falta parentesis de cerrado.\n");
    }
    if(bracketsCount < 0){
        printf("Error, te falta llave de apertura.\n");
    }else if (bracketsCount > 0){
        printf("Error, te falta llave de cerrado.\n");
    }
    if(quotesCount < 0){
        printf("Error, te falta comillas de apertura.\n");
    }else if (quotesCount > 0){
        printf("Error, te falta comillas de cerrado.\n");
    }
}