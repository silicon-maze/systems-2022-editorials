
# **YOU KNOW NOTHING**

Category: Forensics

Author: Vishnu

Answer / Flag: `MAZE{1_D0_kn0w_sOm3_Th1ngs}`  

## Problem Statement

On your jouney you found [this image](https://drive.google.com/file/d/1VWXPL-YyqP36T2pHjIiMICDA8K65C-Ei/view?usp=sharing) and the cat says "YOU KNOW NOTHING JON SNOW".

## Relevant files / links

[image - google drive link](https://drive.google.com/file/d/1VWXPL-YyqP36T2pHjIiMICDA8K65C-Ei/view?usp=sharing)(should be provided to contestant)
[QR Code - google drive link](https://drive.google.com/file/d/1AKZ4WHlQ61EYh0JcWD1wVgzMLCkwEFMC/view?usp=sharing)(should not be provided to contestant)

## Hint

- hint 1: They keep the *Cat's name* a secret
- hint 2: There is an inner image to everyone.


## Solution

The image contains an QR code which can be extracted using [steghide](http://steghide.sourceforge.net/) tool.
The QR code can only be extracted using a password ygritte, which can be concluded from the hints given.
On scanning the QR code you get the flag.
