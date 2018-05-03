# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# a being 1, b being 2, etc.

#alphabet dictionary because we are tiny little b
alphabet = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}

def alphabet_position(text):
    # if bamboozle attempt give them the razzle dazzle.
    if not isinstance(text, str) or text == "":
        return ""
    text = text.lower()
    newString = ""

    # looping trough the text characters checking against my alphabet dictionary
    for i in text:
        for y in alphabet:
            if i == y:
                newString += str(alphabet[y]) + " "
    return newString.strip()


print(alphabet_position(2941718147))