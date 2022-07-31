# **Rescue Mission**

Category: OSINT

Author: Adarsh Kishore

Answer / Flag: `MAZE{W1ntEr_1s-C0m1ngg}`

## Problem Statement

The clans have found that Joffrey Baratheon is planning to attack again. The list of possible people/places which he will attack have been discovered and listed [here](https://drive.google.com/drive/folders/1QvZBKFRyMEL2u2WV1WJSu681dheHOkEs?usp=sharing).

Also, this audio file which might help pinpoint the attack has also been [found](https://drive.google.com/file/d/1CTnV9nDRU4JSv13Ei-QXYO7BlSb-fO4v/view?usp=sharing).

Help them to find Joffrey's next move.

## Relevant files / links

List of images - https://drive.google.com/drive/folders/1QvZBKFRyMEL2u2WV1WJSu681dheHOkEs?usp=sharing

Audio - https://drive.google.com/file/d/1CTnV9nDRU4JSv13Ei-QXYO7BlSb-fO4v/view?usp=sharing

Dragonstone - [image](dragon-stone.jpg)

## Hint

1. The song title is a hint to which of the images is the clue
2. All image files are ultimately binary files, which carry information about it.

## Solution

The given audio can be run through a reverse song analyzer like [Aha-Music](https://www.aha-music.com/identify-songs-music-recognition-online) to get it as 'Dragonstone'. This helps in pinpointing the location as corresponding to [dragon-stone.jpg](dragon-stone.jpg).

On running this image through a hex editor like [HexEd](https://hexed.it), in the very end bytes is the flag `MAZE{W1ntEr_1s-C0m1ngg}`
