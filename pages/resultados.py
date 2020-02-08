from selenium.webdriver.common.by import By


class GoogleResultados:
    RESULTADOS = (By.XPATH, "//div[@class='rc']")

    @classmethod
    def RESULTADOS_ASOCIADOS(cls, palabra):
        xpath = f'//span[@class="st"][contains(text(), "{palabra}")]'
        return (By.XPATH, xpath)

    @classmethod
    def LIGAS_ASOCIADAS(cls, palabra):
        xpath = f'//a[contains(text(), "{palabra}")]'
        return (By.XPATH, xpath)

    def __init__(self, webdriver):
        self.webdriver = webdriver

    def resultados(self):
        resultados = self.webdriver.find_elements(*self.RESULTADOS)
        return resultados

    def resultados_asociados(self, palabra):
        resultados_asociados = self.webdriver.find_elements(*self.RESULTADOS_ASOCIADOS(palabra))
        return resultados_asociados
    
    def ligas_asociadas(self, palabra):
        ligas_asociadas = self.webdriver.find_element(*self.LIGAS_ASOCIADAS(palabra))
        return ligas_asociadas