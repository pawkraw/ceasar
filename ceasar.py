def encrypt(text: str, shift: int) -> str:

    a = ""
    for i in text:
        if i == " ":
            a += "!"
        else:
            a += chr((ord(i) - 65 + shift) % 26 + 65)
    return a


def decrypt(text: str, shift: int) -> str:

    a = ""
    for i in text:
        if i == "!":
            a += " "
        else:
            a += chr((ord(i) - 65 - shift) % 26 + 65)
    return a


print(encrypt("ALA MA KOTA A KOTA NIE MA", 4))

print(decrypt("EPE!QE!OSXE!E!OSXE!RMI!QE", 4))

# Comment
