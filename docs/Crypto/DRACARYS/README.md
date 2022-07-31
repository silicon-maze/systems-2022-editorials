#  **_DRACARYS_ 🔥**

Category: crypto

Author: Sujant :)

Answer / Flag: `MAZE{attack@dusk}`

## Problem Statement

Lannisters and White walkers are battling against each other.
Daenerys plans on taking the opportunity and attack unexpectedly on weakest points during the battle with her dragons. 

She’s sent a message by her followers of the timing when it would be feasible. 

See if you can break it to catch up to her plans.

### Message:
`aDRACARYScDRACARYSuDRACARYStDRACARYSaDRACARYSkDRACARYSdDRACARYSsDRACARYStDRACARYS@DRACARYSk`

## Hint
* It’s an _encrypted_ message, as strong as the de*fence* of the *number* of her dragons.

## Solution

- If looked carefully, the message has DRACARYS throughout the string. 
- It hints it being a repitive text and either a simple python code can be written or can be done manually to remove DRACARYS and rejoining to form a new string which is the encrypted message we need.
- Now, the italic texts hint at _encrypted_ and de**fence** and something about the **number** of her dragons. On search, one can find about RAIL FENCE ENCRYPTION ALGORITHM where the count of rails is required to decode it. Daenerys has **3** dragons which will serve as the rails' count for us.
- We have enough RAIL FENCE ENCRYPTION websites and putting it all together, we get- `attack@dusk`

![DRACARYS_solution_pic](https://user-images.githubusercontent.com/73742938/176682815-f260d419-6c91-40ff-a699-ea0d3aed1edc.png)


### Answer: `MAZE{attack@dusk}`
