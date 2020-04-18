from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleBusqueda:
    URL = 'http:/www.google.com'

    Q_INPUT = (By.NAME, 'q')

    def __init__(self, webdriver):
        self.webdriver = webdriver

    def carga(self):
        self.webdriver.get(self.URL)

    def busqueda(self, palabra):
        q = self.webdriver.find_element(*self.Q_INPUT)
        q.send_keys(palabra + Keys.RETURN)