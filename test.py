import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from variables import *
import warnings
import os


CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH", "./chromedriver")


class Test(unittest.TestCase):
    # method will test page on presence broken links (Page not found)
    def test_page_not_found(self):
        warnings.simplefilter('ignore', ResourceWarning)
        s = Service(CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=s)
        driver.get(url)
        driver.implicitly_wait(15)
        links = driver.find_elements(By.TAG_NAME, 'a')
        link_list = []
        f = open("Page_not_found.txt", "w")
        for item in links:
            lorem_link = item.get_attribute('href')
            link_list.append(lorem_link)
        for link in link_list:
            driver.get(link)
            driver.maximize_window()
            time.sleep(1)
            if "Page not found" in driver.page_source:
                print("Page not found", link, file=f)
        driver.__exit__()

    # this method will test page on presence lorem ipsum text
    def test_lorem_ipsum_text(self):
        warnings.simplefilter('ignore', ResourceWarning)
        s = Service(CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=s)
        driver.get(url)
        driver.implicitly_wait(15)
        links = driver.find_elements(By.TAG_NAME, 'a')
        link_list = []
        f = open("Lorem_text.txt", "w")
        for item in links:
            lorem_link = item.get_attribute('href')
            link_list.append(lorem_link)
        for link in link_list:
            driver.get(link)
            driver.maximize_window()
            time.sleep(2)
            if "Lorem ipsum" in driver.page_source:
                print("Lorem ipsum on webpage", link, file=f)
        driver.__exit__()

    # This method will test items grid on presence broken images "Image not found"
    def test_broken_images(self):
        warnings.simplefilter('ignore', ResourceWarning)
        s = Service(CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=s)
        driver.get(url)
        driver.implicitly_wait(15)
        portmeirion_page = driver.find_element(By.XPATH, '//*[@id="root"]/header/div[2]/ul/li[2]/div/figure/figcaption')
        portmeirion_page.click()
        all_items = driver.find_element(By.XPATH, '//*[@id="root"]/header/div[2]/ul/li[2]/div/div/div/a[1]')
        all_items.click()
        list_of_items = driver.find_elements(By.CLASS_NAME, 'ProductCard-Link')
        link_broken_image = []
        f = open("Image_not_found.txt", "w")
        for item in list_of_items:
            product_link = item.get_attribute('href')
            link_broken_image.append(product_link)
        for link in link_broken_image:
            driver.get(link)
            driver.maximize_window()
            time.sleep(1)
            if "Image not found" in driver.page_source:
                print("Broken image on page", link, file=f)
        driver.__exit__()
