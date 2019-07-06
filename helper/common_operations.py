from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pathsToResources.paths_to_use import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def set_up_chrome(url):
    chrome_folder = Path("chromedriver").resolve() 
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US'})

    driver = webdriver.Chrome(executable_path=chrome_folder, options=options)
    driver.maximize_window()
    driver.get(google_url)

    return driver

def wait_for_element(driver, type_selector, route_element):
    if type_selector == "CSS":
        first_result_page_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, route_element))
        )
    if type_selector == "ID":
        first_result_page_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, route_element))
        )

    return first_result_page_element

def click_element(element, type_selector="", route_element=""):
    if type_selector == "CSS":
        element = element.find_element_by_css_selector(route_element)
        element.click()
    else:
        element.click()

def write_on_element(driver, type_selector, route_element, words):
    if type_selector == "CSS":
        element = driver.find_element_by_css_selector(route_element)
        element.clear()
        element.send_keys(words)

    return element
