import pytest
@pytest.mark.parametrize(
    "palabra, frase",
    [("hola", "hola, mundo"), ("python", "pruebas selenium con python"), ("Lytica", "Hola a todos")])
def test_texto_en_frase(palabra, frase):
    assert palabra in frase