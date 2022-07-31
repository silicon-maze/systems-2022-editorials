# **Tywin's debt**

Category: OSINT

Author: Achintya Kumar

Answer / Flag: `MAZE{7580485c2477617804182b3cd8530da10d0bdb9f7c2bd80c2c3c027379e23ee5}`

## Problem Statement

Tywin has summoned you, a bounty hunter to find a certain man who claims to be the richest in all of westeros. This has created unnecessary rumours which can be bad for the trade.

He needs you to find and report his location back in a encrypted manner as this is a private matter. 
Lannisters prefer SHA-256 for encryption.

The only lead tywin provided you is that the perpetrator is known by his moniker "Richest_in_westeros" on some famous social media platform

Encrypt his coordinates after trimming it to integers, Example: "11.669E,22.1111S" becomes "11E,22S" and is encrypted thereafter.

## Hint

- 'u' stands for users. 

## Solution

Search the user on username search engines, we'll get the reddit account u/Richest_in_westeros. This contains a post which contains "Where richest of richest live. Everyone is rich here" leading us to find the richest country per capita currently which is Luxembourg. 

Search the coordinates for Luxembourg we get `49.8153° N, 6.1296° E` , then trimming it we get`49N,6E` and encrypting it using online sha calculator we get the flag. 
