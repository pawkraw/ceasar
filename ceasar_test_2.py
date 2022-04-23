def encrypt(text: str, shift: int) -> str:
    """Funkcja szyfrująca"""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 25 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 25 + 97)
    return result


def decrypt(text: str, shift: int) -> str:
    """Funkcja deszyfrująca"""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result


if __name__ == "__main__":
    assert encrypt("A", 1) == "B"
    assert decrypt("A", 1) == "Z"
