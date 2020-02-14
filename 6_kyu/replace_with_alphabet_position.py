# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.

def alphabet_position(text):
    output = []
    for char in text:
        if 97 <= ord(char) <= 122:
            output.append(str(ord(char)-96))
        elif 65 <= ord(char) <= 90:
            output.append(str(ord(char)-64))
        else:
            pass
    return " ".join(output)
