import pytest
import os
import sys
sys.path.append(os.pardir)
from helper import int_to_little_endiant


def test_int_to_little_endian():
    actual = int_to_little_endiant(7, 3)
    expected = b'\x07\x00\x00'
    assert actual == expected
    actual = int_to_little_endiant(7, 2)
    expected = b'\x07\x00'
    assert actual==expected

