def alerts(driver):
    """
    Ejemplo de como interactuar con elementos tipo 'alert'
    """
    # URL del ejercicio
    url = "https://www.seleniumeasy.com/test/javascript-alert-box-demo.html"
    
    # Abrimos la URL
    driver.open_url(url)
    
    # Seleccionamos elemento que activa alert 
    
    click_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/button')
    
    click_button.click()
    
    # Seleccionamos el elemento alert emergente
    
    alert = driver.switch_to.alert
    
    alert.accept()
    
    
def popups(driver):
    """
    Ejemplo de como interactuar con componentes emergentes
    """
    
    # URL del ejercicio
    url = "https://phpapps.condusef.gob.mx/condusefhipotecario/datos.php"
    
    # Abrimos la URL
    driver.open_url(url)
    
    
    # Seleccionamos el componente emergente
    elemento_emergente = driver.switch_to.active_element
    
    
    elemento_emergente.find_element_by_class_name('close').click()
    
    