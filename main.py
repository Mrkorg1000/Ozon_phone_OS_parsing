import os 
from dotenv import load_dotenv
import undetected_chromedriver as uc
from functions import *
from selenium.common.exceptions import NoSuchElementException
from phone_xpath_filters import filters
from search_patterns import *
from analytics import get_phone_os_count, create_analytics


load_dotenv()

driver_path = os.getenv('CHROME_DRIVER_PATH')
main_url = os.getenv('MAIN_URL')
            

phone_links = []

phone_os_list = []


def main():
    global phone_links

    driver = uc.Chrome(executable_path=driver_path)
    driver.implicitly_wait(3)

    page_2_url = get_phone_links(driver, main_url, phone_links) # Взяли все с 1-й страницы
    page_3_url = get_phone_links(driver, page_2_url, phone_links) # Взяли все со 2-й страницы
    get_phone_links(driver, page_3_url, phone_links) # Взяли все с 3-й страницы

    driver.quit()
    print(len(phone_links))
    return len(phone_links)


def get_os_info(phone_links_list, filters):
    global phone_os_list

    driver = uc.Chrome(executable_path=driver_path)
    driver.implicitly_wait(3)
    data_length = 0
    for link in phone_links_list:
        
        counter = 0
        for xpath in filters:
            try:
                driver.get(link)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(4)
                os_info = driver.find_element(By.XPATH, xpath) 
                if os_info:
                    if xpath == xpath_2 or xpath == xpath_3:
                        os_info_data = parse_os_info(miui_pattern, os_info.text)
                        print(f'OS_INFO: {os_info_data} \n  {link} \n  {[xpath]}')
                        print('_______________________________________________')
                        phone_os_list.append(os_info_data)
                    else:
                        print(f'OS_INFO: {os_info.text} \n  {link} \n  {[xpath]}')
                        print('_______________________________________________')
                        phone_os_list.append(os_info.text)
                    counter == 0
                    data_length += 1
                    break
            
            except NoSuchElementException:
                pass
                counter += 1
                if counter == 2:
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!LINK {link} needs XPATH revision')
    print(data_length)
           

if __name__ == "__main__":
    main()
    get_os_info(phone_links, filters)
    create_analytics(get_phone_os_count, phone_os_list)

# Пример результата: https://gist.github.com/Mrkorg1000/8139415bf451f8745434970b21c39ef4




