from ..helper import BASE58_ALPHABET,encode_base58
import pytest

def test_base58():
    actual= encode_base58(bytes.fromhex(""))