import unittest
from ceasar_test_2 import encrypt, decrypt


class TestEncrypt(unittest.TestCase):
    def test_simple_encrypt_1(self):
        self.assertEqual(encrypt("A", 1), "B")

    def test_simple_encrypt_2(self):
        self.assertEqual(encrypt("Z", 1), "A")

    def test_simple_encrypt_3(self):
        self.assertEqual(encrypt("CEASAR CIPHER DEMO", 4), "GIEWEV!GMTLIV!HIQS")


class TestDecrypt(unittest.TestCase):
    def test_simple_decrypt_1(self):
        self.assertEqual(decrypt("B", 1), "A")

    def test_simple_decrypt_2(self):
        self.assertEqual(decrypt("A", 1), "Z")

    def test_simple_decrypt_3(self):
        self.assertEqual(decrypt("GIEWEV!GMTLIV!HIQS", 4), "CEASAR CIPHER DEMO")
