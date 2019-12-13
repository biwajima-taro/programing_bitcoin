from chapter1.field_element import FieldElement
import pytest
import os
import sys
sys.path.append(os.pardir)
sys.path.append("../../")


def test_multiply():
    element1 = FieldElement(num=3, prime=13)
    element2 = FieldElement(num=6, prime=13)
    expected = FieldElement(num=5, prime=13)
    assert expected == element1*element2


def test_exponetiation():
    element1 = FieldElement(num=3, prime=13)
    x = 3
    expected = FieldElement(num=1, prime=13)
    assert expected == element1**x


def test_add():
    '''test add in finite field.'''
    element1 = FieldElement(num=3, prime=13)
    element2 = FieldElement(num=6, prime=13)
    actual = element1 + element2
    expected = FieldElement(num=9, prime=13)
    assert actual == expected


def test_add_illegal():
    '''test add in finite field.'''
    element1 = FieldElement(num=3, prime=13)
    element2 = FieldElement(num=6, prime=20)
    with pytest.raises(ValueError):
        actual = element1+element2


def test_default_value():
    '''test with illegal constructor arguments'''
    with pytest.raises(ValueError):
        tmp = FieldElement(num=-123, prime=123)
    with pytest.raises(ValueError):
        tmp2 = FieldElement(num=123, prime=-123)
    with pytest.raises(ValueError):
        tmp3 = FieldElement(num=123.12, prime=1233)

    with pytest.raises(ValueError):
        tmp4 = FieldElement(num=34, prime=123.123)
