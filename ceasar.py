def encrypt(text: str, shift: int) -> str:

    a = ""
    for i in text:
        if i == " ":
            a += "!"
        else:
            a += chr((ord(i) - 65 + shift) % 25 + 65)
    return a


def decrypt(text: str, shift: int) -> str:

    a = ""
    for i in text:
        if i == "!":
            a += " "
        else:
            a += chr((ord(i) - 65 - shift) % 25 + 65)
    return a


