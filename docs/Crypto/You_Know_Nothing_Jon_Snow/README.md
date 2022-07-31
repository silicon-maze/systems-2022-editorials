# *You Know Nothing Jon Snow**

Category: Crypto, Forensic

Author: Advaith

Answer / Flag: `MAZE{weLL_u_d0_NO_smtg_j0n_sN0w}`

## Problem Statement

A wants to send a message to B and Jon Snow wants to read the secret message. A is confident that Jon Snow knows nothing and hence uses a very weak and a baby encryption technique to encrypt the message to send it to B. The secret message is hidden in the below file and that message is symetrically encrypted. Can you find this hidden flag?

## Relevant files / links
Download and analyse the file

[4ensicxorcrypto.jpg](https://drive.google.com/file/d/1ivadDNAEo92sWJzR4nOvqbBZh-unKuQ1/view)

## Hint

- The name of the image file hints about a way to conceal data.
- What does '=' means?
- encoding first, encryption later

## Solution

- The name of the file gives a hint that it is forensic and a crypto question.
- Use _exiftool_ to anaylse the file.
- On analyzing the file, the meta data _License_ contains a _base64_ text. It can be identified with a "==" at the end.
- Decode the base64 text and it will result in a hexadecimal string. Since the problem statement hints that the encryption technique is weak and symmetric, it should be XOR encryption.
- Since single byte XOR can be easily brute forced (as there are only 256 possiblities), the flag will be obtained when the key is 255 (end of the output)

[Solution File](./solution.py)
