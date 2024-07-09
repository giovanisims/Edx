import pytest
from response import validate

def test_validate():
    assert validate("malan@harvard.edu") == "Valid"
    assert validate("my_email@email.com") == "Valid"
    assert validate("malan@@@harvard.edu") == "Invalid"
    assert validate("my_email@email..com") == "Invalid"