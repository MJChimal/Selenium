from base.base_driver import BaseWebDriver


if __name__ == '__main__':
    
    crawler = BaseWebDriver()
    
    crawler.open_url()
    
    crawler.driver.close()