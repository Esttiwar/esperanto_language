# Esperanto

#### Esperanto is a small programming language for handling text files (written in natural language) from the terminal/shell.

#### Features

## word_count

Allows to count the number of words in a text file.

    esperanto ${word_count}(test.txt)

## translate

Translates the content of a text file from one language to another.

    esperanto ${translate from "es" to "en"}(test.txt)(translate.txt)

## speech

Generates an mp3 audio file from the content of a text file.

    esperanto ${speech}("test.txt")("audio.mp3")

## Steps:

1.  Download or clone the repository
2.  You can use the test.txt file or add your own text file.
3.  From the terminal run the `__main__.py` file as follows: python3 `__main__.py`
