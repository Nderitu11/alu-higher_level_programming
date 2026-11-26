#!/usr/bin/python3
"""5-text_indentation module.

Provides text_indentation(text) which prints a text with two new
lines after each of the characters ".", "?" and ":".
"""


def text_indentation(text):
    """Print text with 2 new lines after each ".", "?" and ":".

    No space is printed at the beginning or end of a line.
    Raise TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    lines = [line.strip(" ") for line in result.split("\n")]
    print("\n".join(lines), end="")
