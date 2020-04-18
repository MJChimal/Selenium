import pytest

from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys

from pages.google import GoogleBusqueda
from pages.resultados import GoogleResultados

@pytest.fixture
def webdriver():
    webdriver = Firefox(executable_path='./geckodriver')
    webdriver.implicitly_wait(5)
    yield webdriver
    webdriver.quit()


def test_busqueda_en_google(webdriver):
    palabra = 'space'
    interes = 'space X'

    google = GoogleBusqueda(webdriver)
    google.carga()
    google.busqueda(interes)

    resultados_en_google = GoogleResultados(webdriver)
    assert resultados_en_google.resultados()
    assert resultados_en_google.resultados_asociados(palabra)
