# **Now You Hear Me**

Category: Forensics

Author: Dibyam

Answer / Flag: `MAZE{YOUREARSAREGOOD}`

## Problem Statement

"A good act does not wash out the bad, nor a bad act the good"

In an alternate universe however, A good act does wash out the bad.

## Relevant files / links

[throne.rar](https://drive.google.com/file/d/1TPRSYhJDsq8rhluw6Z7wddIjbbECn5a5/view?usp=sharing)

[throne.jpg](https://drive.google.com/file/d/1tilA_Vc1HeQab5wIcQ5iHZINZXexSu_U/view?usp=sharing)

## Hint

Usually they say, that the truth is good and the lie is bad. I wonder why

## Solution

- Open throne.jpg with any text editor and scroll to the bottom. You see the words - "Who do I belong to"
- The answer to this question is "bran". This is the password for the archive.
- After unzipping the archive with "bran" as the password, you see two mp3 files, both sounding almost identical. 
- The file named "hear_me_out.mp3" however has been superimposed with a morse signal, which is faintly audible. 
- The other audio file, is the original audio file (The Truth)
- As far as all the good cancelling all the bad goes, invert the given original audio track and superimpose it with the other "hear_me_out.mp3" file. 
- The same frequencies in the both the files would cancel each other, and only the morse code would remain. 
- Now, you can open the audio file using any Audio Visualizing tool such as Audacity and see the spectogram. To get a clear picture, reduce the window size to around 256 and reduce the range to around 20dB. This will reveal the hidden morse code which looks something like this. 

- ![](https://www.linkpicture.com/q/Screenshot-2022-07-01-231127.png)
- The Dits and Dahs are clearly visible. Feed them into any morse decoder and you get the final flag as `YOUREARSAREGOOD`
