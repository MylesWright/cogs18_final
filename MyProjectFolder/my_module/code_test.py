import pytest

from password_checker import find_cap_lett



def test_answer():
    assert find_cap_lett("Capital") == 1
    assert find_cap_lett("capital") == 0
    assert find_cap_lett("ALLCAPS") == 7 


