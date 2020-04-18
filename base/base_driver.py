import os

import json

from dataclasses import dataclass, field

from typing import Any

from selenium import webdriver

PATH_CONFIGS = os.path.join(os.environ.get('PWD'), 'config.json')

with open(PATH_CONFIGS) as f:
  CONFIGS = json.load(f)


def lauch_driver():
    browser = CONFIGS.get('browser').capitalize()
    headless = CONFIGS.get('headless')
    executable_path = CONFIGS.get('executable_path')

    options = getattr(webdriver, f"{browser}Options")()
    if headless:
        options.add_argument('--headless')
    return getattr(webdriver, f"{browser}")(
        executable_path=executable_path, options=options
    )
    
@dataclass
class BaseWebDriver:
    
    driver: Any = field(default_factory=lauch_driver)
    
    def open_url(self, url):
        
        self.driver.get(url)
        
    