import pytest

def test_existencia_elemento():
    with pytest.raises(FileNotFoundError):
        open('pruebas_selenium.py', 'r')