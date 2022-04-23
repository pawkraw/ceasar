from ceasar import encrypt, decrypt

text = "ALA MA KOTA A KOTA NIE MA"
shift = 4

assert decrypt(encrypt(text, shift), shift) == "ALA MA KOTA A KOTA NIE MA"
assert encrypt("A", 1) == "B"
assert decrypt("A", 1) == "Z"
