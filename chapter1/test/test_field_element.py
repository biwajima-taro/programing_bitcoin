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


def test_add_illegal():
    '''test add in finite field.'''
    element1 = FieldElement(num=3, prime=13)
    element2 = FieldElement(num=6, prime=20)
    with pytest.raises(ValueError):
        actual = element1+element2

def test_default_value():
	'''test with illegal constructor arguments'''
	with pytest.raises(ValueError):
		tmp=FieldElement(num=-123,prime=123)
	with pytest.raises(ValueError):
		tmp2=FieldElement(num=123,prime=-123)
