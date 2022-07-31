#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lib.h"

DEFINE_HIDDEN_STRING(Flag, 0x7f, ('M')('A')('Z')('E')('{')('8')('U')('r')('N')('_')('7')('H')('3')('M')('_')('A')('1')('1')('}'));

// To compile with debug flags: gcc -g -o main main.c


int userInput(){
    char * user_answer = malloc(sizeof(char) * 301);
    scanf("%300s", user_answer);
    printf("Are you sure this is your answer:");
    fflush(stdout);
    char flag[30];                             // creating a flag variable to store the flag in the stack.
    char * temp = GetFlag();                   // getting flag and storing it in stack. 
    for(int i = 0; i<strlen(temp); i++){
        flag[i] = temp[i];
    }
    printf(user_answer);                       // printing the user answer to confirm.
    fflush(stdout);
    return 0;
}

int main() {
    printf("You want to find the Secret?[Enter]");
    fflush(stdout); 
    getchar();
    fflush(stdout);
    printf("A riddle first:\nIn a room sit three great men, a king, a priest, and a rich man with his gold.\nBetween them stands a sellsword, a little man of common birth and no great mind.\nEach of the great ones bids him slay the other two. \'Do it,\' says the king, \'for I am your lawful ruler.\'\n\'Do it,\' says the priest, \'for I command you in the names of the gods.\'\n'Do it,\' says the rich man, \'and all this gold shall be yours.\'\nSo tell me - who lives and who dies?\n\n");
    fflush(stdout);
    userInput();
    printf("[Enter]");
    fflush(stdout);
    getchar();
    getchar();    
    printf("Ha you really thought it was that easy to get the flag? I would never give it to you.\n\n\n");
    fflush(stdout);

}
