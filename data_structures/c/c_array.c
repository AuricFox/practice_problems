#include <stdio.h>
#include <stdlib.h>

int main(){
    // Declare an array of integers
    int numbers[5];
    
    // Assign values to the array elements
    numbers[0] = 10;
    numbers[1] = 20;
    numbers[2] = 30;
    numbers[3] = 40;
    numbers[4] = 50;
    
    // Access and print array elements
    printf("Array Elements: ");
    for (int i = 0; i < 5; i++) { 
        printf("%d ", numbers[i]);
    }
    printf(" \n");

    // Declare an array of strings
    // Maximum length of each string is set to 20 characters
    char strings[3][20];
    
    // Assign values to the array elements
    strcpy(strings[0], "Hello");
    strcpy(strings[1], "World");
    strcpy(strings[2], "C Programming");
    
    // Access and print array elements
    printf("Array Elements: ");
    for (int i = 0; i < 3; i++) { 
        printf("%s ", strings[i]);
    }
    printf(" \n");
    
    return 0; 
}