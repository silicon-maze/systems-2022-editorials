# The Three-Eyed Raven's Riddle

Category: RE/PWN

Author: Amogh Umesh

Answer / Flag: MAZE{100k_f02_m3_83n347h_7h3_tr33}

## Problem Statement

The three eyed raven is flying over the seven kingdoms when it starts to feel thirsty. It looks down and finds a pitcher half filled with water. It tries to drink the water but is unable to as the water level is too low. Help the three eyed raven to drink the water. The working of the pitcher is given in the code below.

## Relevant files / links
Source code(given to participants): https://drive.google.com/file/d/1mP-o3Nu7_LzGa536PyyAax1EP-XXvAU8/view?usp=sharing \
Executable link(given to participants): https://drive.google.com/file/d/1CtSj2aXmA6TpNPlWWNqDTae9iAE8HfhC/view?usp=sharing


## Solution

Relating to the age old story of the crow and the pitcher, the bird must overflow the water hinting in a way this is a buffer overflow question. Reading the code we find the vulnerability on line 25.
By analysing the code we know the only way to get the flag is to pass the if statement on line 31. Since we don't know the contents of secretPassword variable the only way to pass the check is to alter the contents through buffer overflow.
The arrangement of malloc statements puts the location of secretPassword just after the flag variable which is susceptible to buffer overflow. 
Inorder to overwrite the secretPassword the input must have a length of atleast 36 bytes (20 for flag, 4 for secretPassword, 4 bytes for book keeping and 8 bytes unallocated space between them). 
Therefore in the Enter Username prompt, an input like AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA. The last 4 characters overwrites the secretPassword. Since the password type is an integer, we have to convert the AAAA to an integer. Doing so we get 1094795585. 
Putting this number for password will pass the check and the flag will be revealed.
