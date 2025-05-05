from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from config import BRAVE_PATH, CHROMEDRIVER_PATH, PAGE_LOAD_WAIT
import time

def config_driver():
    options = Options()
    options.binary_location = BRAVE_PATH
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    service = Service(executable_path = CHROMEDRIVER_PATH)
    return webdriver.Chrome(service = service, options=options)

def fetch_page_source(url):
    driver = config_driver()
    driver.get(url)
    time.sleep(PAGE_LOAD_WAIT)
    page_source = driver.page_source
    driver.quit()
    return page_source