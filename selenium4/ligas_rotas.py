import requests 

def ligas_rotas(driver):
    
    links = driver.find_elements_by_tag_name('a')
    images = driver.find_elements_by_tag_name('img')

    for link in links:
        r = requests.head(link.get_attribute('href'))
        if r.status_code != 200:
            print(r)
            
    # Hacer lo mismo con imagenes