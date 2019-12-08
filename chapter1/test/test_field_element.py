import pytest
import os
import sys
sys.path.append(os.pardir)
from field_element import FieldElement


def test_add():
    '''test add in finite field.'''
    element1 = FieldElement(num=3, prime=13)
    element2 = FieldElement(num=6, prime=13)
    actual = element1 + element2
    expected = FieldElement(num=9, prime=13)
    assert actual == expected


def test_illegal():
    '''test add in finite field.'''
    element1 = FieldElement(num=3, prime=13)
    element2 = FieldElement(num=6, prime=20)
    with pytest.raises(ValueError):
        actual = element1+element2
