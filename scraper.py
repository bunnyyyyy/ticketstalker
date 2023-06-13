from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



import random
import time

proxy = "124.240.187.80:82"

webdriver.DesiredCapabilities.CHROME['proxy'] = {
   "httpProxy":proxy,
   "ftpProxy":proxy,
   "sslProxy":proxy,
   "noProxy":None,
   "proxyType":"MANUAL",
   "class":"org.openqa.selenium.Proxy",
   "autodetect":False
}


driver = uc.Chrome()

driver.get("https://nowsecure.nl")

# driver.get("https://seatgeek.com/taylor-swift-with-haim-and-gracie-abrams-tickets/santa-clara-california-levi-s-stadium-2023-07-28-6-30-pm/concert/5862048")

time.sleep(10)

#driver.get("https://nowsecure.nl")

# try:
#     desired_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__next .MappedEventLayout__MapPage-sc-c5b97ed1-0.hOHnAR .MapAndListingsLayout__DesktopWrapper-sc-2188243b-0.iXTtTd .Omnibox__PanelWrapper-sc-2ba63abd-1.eZDNqq .presenters__ViewColumn-sc-de03606d-0.dISTYK [data-test="all-listings"] [aria-label*=" ticket"]')))
#     print("worked")

# except TimeoutError:
#     print("element not here")

# time.sleep(5)
#desired_element = driver.find_element(By.CSS_SELECTOR, '#__next .MappedEventLayout__MapPage-sc-c5b97ed1-0.hOHnAR .MapAndListingsLayout__DesktopWrapper-sc-2188243b-0.iXTtTd')


# start-of-content > div.Omnibox__PanelWrapper-sc-2ba63abd-1.eZDNqq > div.presenters__ViewColumn-sc-de03606d-0.dISTYK > div > div:nth-child(5) > div
# 
#  #__next .MappedEventLayout__MapPage-sc-c5b97ed1-0.hOHnAR .MapAndListingsLayout__DesktopWrapper-sc-2188243b-0.iXTtTd .Omnibox__PanelWrapper-sc-2ba63abd-1.eZDNqq .presenters__ViewColumn-sc-de03606d-0.dISTYK [data-test="all-listings"] [aria-label*="ticket at"]

# text = desired_element.get_attribute('aria-label')
# print(text)

# driver.quit()
