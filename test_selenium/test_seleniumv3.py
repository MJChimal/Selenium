import json
import pytest

from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.common.keys import Keys

from pages.google import GoogleBusqueda
from pages.resultados import GoogleResultados


@pytest.fixture(scope='session')
def config():
  with open('config.json') as config_file:
    data = json.load(config_file)
  return data

@pytest.fixture(scope='session')
def config_wait_time(config):
    print(config['wait_time'])
    return config['wait_time'] if 'wait_time' in config else 5


@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('El archivo de configuración no contiene "browser"')

    elif config['browser'] not in ['chrome', 'firefox']:
        raise Exception(f'"{config["browser"]}" explorador no soportado')

    return config['browser']


@pytest.fixture
def webdriver(config_browser, config_wait_time):
    if config_browser == 'chrome':
        webdriver = Chrome()

    elif config_browser == 'firefox':
        webdriver = Firefox(executable_path='./geckodriver')

    else:
        raise Exception(f'"{config_browser}" no es soportado')

    webdriver.implicitly_wait(config_wait_time)

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

