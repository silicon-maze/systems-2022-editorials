# **Secret Meeting**

Category: Crypto

Author: Adarsh Kishore

Answer / Flag: `MAZE{meEt_@_W1nter_del1}`

## Problem Statement

Jon Snow is organizing a secret meetings of the rulers of the **seven** kingdoms to
organise a plan to defeat the **three**-headed dragon Targaryn. In order that the spies of the dragon do not discover this, he sends a coded message `8437385373703739737382373883731163731163739037385373863734837388373483736637310237386373122373703731173731003737137386373121373883735037382373108373983736837370373573736137361` to everyone. To find the location, you must decode it. There is also a scroll accompanied with it: **remember the most important numbers in our world.**

## Hint

1) There is a number occuring quite frequently in the message. 

2) Does the "==" at the end tell you something?

## Solution

The given text has `373` acting as a separator. If we `split()` it with `373` as a delimeter,
we will get `['84', '85', '70', '97', '82', '88', '116', '116', '90', '85', '86', '48', '88', '48', '66', '102', '86', '122', '70', '117', '100', '71', '86', '121', '88', '50', '82', '108', '98', '68', '70', '57', '61', '61']`.

On converting each number to its ASCII equivalent and joining the characters, we get `TUFaRXttZUV0X0BfVzFudGVyX2RlbDF9==`. The `==` at the end suggests `base64` encoding.

On decoding it in `base64`, we get the flag `MAZE{meEt_@_W1nter_del1}`. The process is outlined in [solution.py](solution.py).
