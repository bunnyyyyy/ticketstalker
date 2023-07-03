from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



import random
import time



url = "https://seatgeek.com/taylor-swift-with-haim-and-gracie-abrams-tickets/santa-clara-california-levi-s-stadium-2023-07-28-6-30-pm/concert/5862048"


driver = webdriver.Safari()


driver.get(url)

time.sleep(10)


try:
    desired_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__next .MappedEventLayout__MapPage-sc-c5b97ed1-0.hOHnAR .MapAndListingsLayout__DesktopWrapper-sc-2188243b-0.iXTtTd .Omnibox__PanelWrapper-sc-2ba63abd-1.eZDNqq .presenters__ViewColumn-sc-de03606d-0.dISTYK [data-test="all-listings"] [aria-label*=" ticket"]')))
    print("worked")

except TimeoutError:
    print("element not here")



print(desired_element)

price = desired_element.get_attribute("aria-label")
print(price)

driver.quit()
