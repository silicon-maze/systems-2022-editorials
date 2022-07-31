#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lib.h"
DEFINE_HIDDEN_STRING(Flag, 0x7f, ('M')('A')('Z')('E')('{')('1')('0')('0')('k')('_')('f')('0')('2')('_')('m')('3')('_')('8')('3')('n')('3')('4')('7')('h')('_')('7')('h')('3')('_')('t')('r')('3')('3')('}'));
DEFINE_HIDDEN_STRING(Secret, 0x7f, ('-')('2')('1')('0')('9')('1')('6')('2')('1')('1')('5'));

//The right username will release the secrets

int main() {
    char * username = malloc(sizeof(char) * 20);
    int * secretPassword = malloc(sizeof(int));

    char * flag = GetFlag();               // getting flag from environment variable
    char * secret = GetSecret();           // getting secretPassword from environment variable
    if(flag == NULL || secret == NULL){
        printf("Error: Flag or Secret not found\n");  // If encountering this error. Set environment variable "Flag" to a string and variable "Secret" to an integer.
        return 1;
    }
    *secretPassword = atoi(secret);             // password is an int.   
    
    int password;
    printf("Enter username: ");
    fflush(stdout);                 
    char buf[1000];
    scanf("%s", buf);                           // getting username from user

    strcpy(username, buf);

    printf("Enter password: ");
    fflush(stdout);
    scanf("%d", &password);                     // getting password from user

    if (*secretPassword == password) {          // if password is correct, print the flag.
        printf("Flag: %s\n", flag);
    } else {
        puts("I guess you're not cool enough to see the flag.");
    }
    return 0;
}
