# **Needle In A Haystack**

Category: Web

Author: Kavya Bhat

Answer / Flag: `MAZE{th3_N33dl3}`

## Problem Statement

Joffrey finds himself in an interesting armory, where he can view what weapon Jon Snow and Jorah Mormont will be wielding in the next battle. However, he _comments_ that he is unable to see which weapon Arya Stark wields. He suspects that Arya may have hidden her _data_ from view. Help Joffrey find Arya's weapon. 

## Relevant files / links

[Website](https://needle-in-haystack.herokuapp.com/)<br>
[Source code](https://drive.google.com/file/d/1Q66CgHu3YX9ud2Ppnej-N5xNYw92sdur/view?usp=drivesdk) 

## Hints

1. Where are data and records stored?
2. Joffrey is probably too serious about this. Does he need to _inject_ humor into his _comments_?

## Solution

On searching for _Jon Snow_, _Jorah Mormont_ and _Arya Stark_ using the form given, we see that no result shows up for Arya Stark. Considering the problem statement, we can infer that the SQL query sent to the database might be the point at which the input is filtered. 

Examine the source code given. Part of the condition is given to be `AND warrior <> 'Arya Stark'`. Maybe we can comment that section out. SQL comments are signified by `--`. End the input value using a single quote and comment out the rest of the query using `--`. Enter `Arya Stark'--` in the search box, and obtain the flag.

