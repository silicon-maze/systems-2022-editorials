# **Sacred Key**

Category: Forensics

Author: Tejaswi Hegde

Answer / Flag: `MAZE{Pow3r_1s_p0wer}`

## Problem Statement

You happen to come accross this strange looking image. It seems as if there is something hidden in it. Maybe you need a key to unlock the answer.

## Relevant files / links

[the image file](keypic.jpg)

Google Drive - https://drive.google.com/file/d/1xPfTCuD7GqNYI2j9tFD-2ULDb6SU-iVx/view?usp=sharing

## Hint

Hint 1: Maybe the file does not contain just image data. A thorough analysis might reveal answers.

Hint 2: Text can also be encoded into images in a very clever way.

## Solution

Opening the image in a text editor (like Notepad) and scrolling to the end reveals the message "There are 2 prime numbers assosciated with this image. Multiply them and add a .ddns.net at the end. Also remember Romeo Charlie II.".

The primes numbers are the dimensions of the image: 571 x 431 = 246101

Going to 246101.ddns.net gives us a encoded text: ea3c49872517df291aa780125e42ec61361ab37db9ad0a8d

Coming back to the image, running it through an image analyzer (Like [Aperi Solve](https://aperisolve.fr/)) / steganography software (steghide) gives us the message "the key is winteriscoming".

Decoding the text in the jpg file,
Romeo = R,
Charlie = C,
II = 2,
which gives us RC2 encryption.

Using the key "winteriscoming", we can decode the text (RC2 decrypt on a website like [Cyberchef](https://gchq.github.io/CyberChef/)) to get the flag.
