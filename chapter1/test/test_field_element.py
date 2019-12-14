import sys
import os
sys.path.append(os.pardir)
sys.path.append("../../")
from chapter1.field_element import FieldElement
import pytest



def test_multiply():
    element1 = FieldElement(num=3, prime=13)
    element2 = FieldElement(num=6, prime=13)
    expected = FieldElement(num=5, prime=13)
    actual = element1 * element2
    assert expected == actual  # element1*element2
    not_expected = FieldElement(num=3, prime=13)
    assert not_expected != actual
    
def test_exponetiation():
    element1 = FieldElement(num=3, prime=13)
    x = 3
    expected = FieldElement(num=1, prime=13)
    actual = element1**x
    assert expected == actual
    not_expected = FieldElement(num=2, prime=13)
    assert not_expected !=actual

def test_add():
    '''test add in finite field.'''
    element1 = FieldElement(num=3, prime=13)
    element2 = FieldElement(num=6, prime=13)
    actual = element1 + element2
    expected = FieldElement(num=9, prime=13)
    assert actual == expected
    not_expected = FieldElement(num=3, prime=13)
    assert not_expected != actual


def test_add_illegal():
    '''test add in finite field.'''
    element1 = FieldElement(num=3, prime=13)
    element2 = FieldElement(num=6, prime=20)
    with pytest.raises(ValueError):
        element1+element2


def test_default_value():
    '''test with illegal constructor arguments'''
    with pytest.raises(ValueError):
        FieldElement(num=-123, prime=123)
    with pytest.raises(ValueError):
        FieldElement(num=123, prime=-123)
    with pytest.raises(ValueError):
        FieldElement(num=123.12, prime=1233)
    with pytest.raises(ValueError):
        FieldElement(num=34, prime=123.123)
