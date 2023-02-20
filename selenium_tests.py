from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service("/Users/bberreby/Downloads/chromedriver_mac64/chromedriver"))


driver = webdriver.Chrome(executable_path="/Users/bberreby/Downloads/chromedriver_mac64/chromedriver")
driver.get('file:///Users/bberreby/PycharmProjects/tip_calc/index.html')
driver.find_element(By.ID, 'billamt').send_keys('100')
driver.find_element(By.ID, 'serviceQual').send_keys('20')
driver.find_element(By.ID, 'peopleamt').send_keys('4')
driver.find_element(By.ID, 'calculate').click()
tip_value = driver.find_element(By.XPATH, '//*[@id="tip"]').text

assert tip_value == '6.00'
# if tip_value == '5.00':
#     print('OK')
# else:
#     print('Failed')
