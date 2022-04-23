def encrypt(text, shift):

    a = ""
    for i in text:
        if i == " ":
            a += "!"
        else:
            a += chr((ord(i) - 65 + shift) % 25 + 65)
    return a


def decrypt(text, shift):

    a = ""
    for i in text:
        if i == "!":
            a += " "
        else:
            a += chr((ord(i) - 65 - shift) % 25 + 65)
    return a


