from ceasar_test_2 import encrypt, decrypt


class TestEncrypt:
    def test_simple_encrypt_1(self):
        assert encrypt("A", 1) == "B"

    def test_simple_encrypt_2(self):
        assert encrypt("Z", 1) == "A"

    def test_simple_encrypt_3(self):
        assert encrypt("CEASAR CIPHER DEMO", 4) == "GIEWEV!GMTLIV!HIQS"


class TestDecrypt:
    def test_simple_decrypt_1(self):
        assert decrypt("B", 1) == "A"

    def test_simple_decrypt_2(self):
        assert decrypt("A", 1) == "Z"

    def test_simple_decrypt_3(self):
        assert decrypt("GIEWEV!GMTLIV!HIQS", 4) == "CEASAR CIPHER DEMO"
