from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import random
import time


uc = webdriver.Chrome()

uc.get("https://seatgeek.com/taylor-swift-with-haim-and-gracie-abrams-tickets/santa-clara-california-levi-s-stadium-2023-07-28-6-30-pm/concert/5862048")


desired_element = uc.find_element(By.CSS_SELECTOR, '#__next .MappedEventLayout__MapPage-sc-c5b97ed1-0.hOHnAR .MapAndListingsLayout__DesktopWrapper-sc-2188243b-0.iXTtTd')

#sdffaf
#   .Omnibox__PanelWrapper-sc-2ba63abd-1.eZDNqq .presenters__ViewColumn-sc-de03606d-0.dISTYK [data-test="all-listings"] [aria-label*="ticket at"]
#text = desired_element.get_attribute('aria-label')
print("h")

# driver.quit()
