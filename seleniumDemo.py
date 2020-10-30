import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

PATH = "/home/solomondenning/Documents/Q Project/Workshop/Web Crawling/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)  # Optional argument, if not specified will search path.

# ChromeDriver website example code:
#driver.get('http://www.google.com/');
#time.sleep(5) # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('UC Merced')
#search_box.submit()
#time.sleep(5) # Let the user actually see something!
#driver.quit()

# TechWithTim example code:
driver.get('http://www.example.com/')
print('Getting Title: ')
print(driver.title)

print('\nGetting Header: ')
search = driver.find_element_by_tag_name('h1')
print(search.text)

print('\nGetting Text: ')
search = driver.find_element_by_tag_name('p')
print(search.text)

print('\nGetting Hyperlink: ')
search = driver.find_element_by_partial_link_text('...')
print('Visting Hyperlink @ ' + search.text)
time.sleep(3)
search.click()

#print(driver.page_source)

time.sleep(5) # Let the user actually see something!
driver.quit()

