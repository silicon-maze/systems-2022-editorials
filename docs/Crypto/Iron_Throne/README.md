# **Successor to the Iron Throne**

Category: Crypto

Author: Pratik Jallan

Answer / Flag: `MAZE{BraNStark}`

## Problem Statement

Purportedly made from a thousand swords and knives, the Iron Throne is a massive and asymmetrical tangle of jagged and twisted blades, in which reclining is impossible.

However, these blades information. The swords so twisted as if to represent nothingness, a zero, while the knives so fine and straight. The following information was engraved on the iron throne:

- https://drive.google.com/file/d/1S6ap2YfUB6p16zXA67sB3g5-w43ZPeJ5/view?usp=sharing

However, only the true successor to the Iron Throne can access the information. The key is associated to the sum of the most important numbers in Westeros. The key is of the format: `MAZE{message}`

## Hint

- The number of blades might have to do with something with a  monoalphabetic cipher.

## Solution

The user must first access the file. The password is 3 + 7, the two most important numbers in Westeros.

After that, they obtain a file with swords and knives written as the engraving. Swords represent a 0 as stated in the question, while knife a 1. Decode it accordingly to obtain a binary string.

Convert it into a character string, and then apply caesar cipher using 1000 as the key. You know the name of the true successor to the Iron Throne.
