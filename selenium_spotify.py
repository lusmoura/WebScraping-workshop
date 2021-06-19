import re
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    ''' Create a driver '''
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    return driver

def get_element(driver, xpath):
    ''' Get element, waiting for it to appear on screen '''
    return  WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))

def make_request(url, driver):
    ''' Make request with the selenium module '''
    driver.get(url)

def search_artist(artist, driver):
    ''' Use search bar to search for an artist and go to the page '''
    url = 'https://open.spotify.com/search'
    make_request(url, driver)

    search_tab = get_element(driver, '//input[@data-testid="search-input"]')
    search_tab.send_keys(artist)

    artist_result = get_element(driver, '//a[@class="f7ebc3d96230ee12a84a9b0b4b81bb8f-scss"]')
    new_url = artist_result.get_attribute('href')

    make_request(new_url, driver)

def get_listeners(driver):
    ''' In the artist page, get the number of monthly listeners '''
    listeners_tag = get_element(driver, '//span[@class="_85aaee9fc23ca61102952862a10b544c-scss"]')
    listeners = listeners_tag.text
    return listeners

if __name__ == '__main__':
    artist = 'Oasis'

    main_url = 'https://open.spotify.com/search'
    
    driver = get_driver()
    search_artist(artist, driver)
    listeners = get_listeners(driver)
    print(listeners)
    driver.quit()