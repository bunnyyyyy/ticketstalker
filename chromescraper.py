from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager as GM



import random
import time

# options = Options()
# proxy_server_url = "51.81.88.73"
# options.add_argument(f'--proxy-server={proxy_server_url}')

# options = uc.ChromeOptions()
# options.user_data_dir = ""

url = "https://seatgeek.com/taylor-swift-with-haim-and-gracie-abrams-tickets/santa-clara-california-levi-s-stadium-2023-07-28-6-30-pm/concert/5862048"


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(profile, executable_path=GM().install())

#user_data_dir='/Users/nmunjal/Library/Application Support/Google/Chrome/Profile 9'

# driver.get("https://nowsecure.nl")

driver.get(url)

time.sleep(10)


try:
    desired_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__next .MappedEventLayout__MapPage-sc-c5b97ed1-0.hOHnAR .MapAndListingsLayout__DesktopWrapper-sc-2188243b-0.iXTtTd .Omnibox__PanelWrapper-sc-2ba63abd-1.eZDNqq .presenters__ViewColumn-sc-de03606d-0.dISTYK [data-test="all-listings"] [aria-label*=" ticket"]')))
    print("worked")

except TimeoutError:
    print("element not here")


price = desired_element.get_attribute("aria-label")

print(desired_element)
print(price)

driver.quit()
