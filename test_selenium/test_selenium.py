import pytest

from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def webdriver():
    webdriver = Firefox(executable_path='./geckodriver')
    webdriver.implicitly_wait(5)
    yield webdriver
    webdriver.quit()


def test_busqueda_en_google(webdriver):
    url = 'http://www.google.com'
    palabra = 'space'
    interes = 'space X'

    webdriver.get(url)

    q = webdriver.find_element_by_name('q')
    q.send_keys(interes + Keys.RETURN)

    resultados = webdriver.find_elements_by_xpath("//div[@class='rc']")
    assert resultados 

    resultados_asociados = webdriver.find_elements_by_xpath(f'//span[@class="st"][contains(text(), "{palabra}")]')
    assert resultados_asociados


def test_prueba():
    assert 1 > 2
