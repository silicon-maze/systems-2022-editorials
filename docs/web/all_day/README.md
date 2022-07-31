# **All day**

Category: WEB

Author: Vinayak Vatsalya J 

Answer / Flag: `MAZE{4U70M47E_7hE_80R1Ng_57UFf}`

## Problem Statement

Danaerys is looking for banners that will come to her support in westeros. She needs to find which banner will come to her aid, but since there are a lot of kingdoms, she needs to find a way to do it faster.One of her domains has the banner. [Site](https://62a747f9552b2d4f11719650--coruscating-heliotrope-79f6f5.netlify.app/389251.html)

Help her look through all the domains in her kingdom to find the banner that will be her strongest ally.

## Relevant files / links

[Site](https://62a747f9552b2d4f11719650--coruscating-heliotrope-79f6f5.netlify.app/389251.html)

## Solution

The given site reads ```bad luck, try 84851```, on changing the url and going to [same url but with 84851.html](https://62a747f9552b2d4f11719650--coruscating-heliotrope-79f6f5.netlify.app/84851.html) , we get this ``` bad luck, try 4629``` and so on. We get this pattern. 

To get the flag we can write a simple script to parse through each page and go to the next page if theres no flag in the page. 

```
import requests , re
number_pattern = "[0-9][0-9]+"
x = ""
num = "84851"
while "MAZE" not in x:	
	print(f"Visiting {num}")
	url = f"https://62a747f9552b2d4f11719650--coruscating-heliotrope-79f6f5.netlify.app/{num}.html"
	x = requests.get(url).text
	num  = re.findall(number_pattern, x)[0]
	
print(x)
```
Which gives the flag on the last site, ``MAZE{4U70M47E_7hE_80R1Ng_57UFf}``. 

