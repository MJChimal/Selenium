from selenium.webdriver.common.by import By


class GoogleResultados:
    RESULTADOS = (By.XPATH, "//div[@class='rc']")

    @classmethod
    def RESULTADOS_ASOCIADOS(cls, palabra):
        xpath = f'//span[@class="st"][contains(text(), "{palabra}")]'
        return (By.XPATH, xpath)

    def __init__(self, webdriver):
        self.webdriver = webdriver

    def resultados(self):
        return self.webdriver.find_elements(*self.RESULTADOS)

    def resultados_asociados(self, palabra):
        return self.webdriver.find_elements(*self.RESULTADOS_ASOCIADOS(palabra))
    