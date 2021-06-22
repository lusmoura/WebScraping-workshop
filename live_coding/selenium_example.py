from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

url = 'https://open.spotify.com/search'
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get(url)

xpath = '//input[@class="_748c0c69da51ad6d4fc04c047806cd4d-scss f3fc214b257ae2f1d43d4c594a94497f-scss"]'
search_bar = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
search_bar.send_keys('oasis')

xpath = '//a[@class="f7ebc3d96230ee12a84a9b0b4b81bb8f-scss"]'
artist = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
url = artist.get_attribute('href')
driver.get(url)

xpath = '//span[@class="_85aaee9fc23ca61102952862a10b544c-scss"]'
listeners_tag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
listeners = listeners_tag.text
print(listeners)

driver.quit()