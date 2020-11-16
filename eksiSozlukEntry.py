from selenium import webdriver 
import time

search = input("Ekside arama yapmak istediginiz kelime: ")

browser= webdriver.Chrome()

url = "https://eksisozluk.com"

browser.get(url)

time.sleep(3)

aramaButonu= browser.find_element_by_xpath("//*[@id='search-textbox']")

aramaButonu.send_keys(search)

ara= browser.find_element_by_xpath("//*[@id='search-form']/button")

ara.click()

time.sleep(2),

elements = browser.find_elements_by_class_name('content')

for element in elements:
    print(element.text)
    print("***************************************************")


browser.close()

