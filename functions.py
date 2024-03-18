import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from phone_xpath_filters import *


def add_phone_links(links_list, link_elements):
    for link in link_elements:
        href = link.get_attribute('href')
        
        if len(links_list) < 100:
            links_list.append(href)
        else:
            break


def get_next_page_link(driver):
    next_button = driver.find_element(By.LINK_TEXT, 'Дальше')
    next_link = next_button.get_attribute('href')
    print(f'NEXT PAGE !!!!!!!!!!!!!! {next_link}')
    return next_link


def get_phone_links(driver, url, phone_links):
    phone_link_xpath = "//div[contains(@class,'wi0')]/a[starts-with(@href,'/product/')]"
    
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    phone_link_elements = driver.find_elements(By.XPATH, phone_link_xpath)
    next_page_link = get_next_page_link(driver)
    add_phone_links(phone_links, phone_link_elements)
    return next_page_link




