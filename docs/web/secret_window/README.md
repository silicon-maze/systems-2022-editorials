# **Secret Window**

Category: Web

Author: Sudarshan

Answer / Flag: `MAZE{n0_fac3_n0_sp4ce}`

## Problem Statement

On one of Arya Stark's tasks to become a Faceless Man, she is instructed to find a flag which can be seen through a secret window. As a clue to locate the window, she has the following message from the Faceless Man:

Use your imagination, little guest \
Take a thousand-and-ninety steps to the west \
Follow the path and do your best \
to the secret window which lies there in its responsive might \
Hiding the truth from the seeker's sight 

Can you help Arya find the flag?

## Relevant files / links

[Website Link](https://dapper-chimera-58c394.netlify.app/)

## Hints

Use The Faceless man's clue carefully. 

## Solution

Now, there are different ways to get to the flag. But it's first important to understand what lies within the problem. In the website, at first glance, you may just see gibberish text that does not make sense nor does it have any structure. However, if you read the Faceless Man's clue, you see that a few characters are in Caps, specifically UTF and H. Now, "UTF" atleast is something that we've either seen or heard of somewhere; it stands for the Unicode Transformation Format.

When you plug in the gibberish text into a UTF decoder, you may find that there is a weird character placed in between normal characters. This is the Zero-Width Space character (UTF code: `200B`). It isn't visible to the normal user normally, but is visible once you pass it through a UTF decoder, or if you copy paste the source into some editor like VS Code. Pick the character right before the Zero-Width Space, and you get the flag.
