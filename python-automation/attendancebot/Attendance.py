from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = ''
attendance_url = ''

driver = webdriver.Chrome(r"")
driver.get(url)

sign_in = driver.find_element_by_xpath('//*[@id="gb_70"]')
sign_in.click()

email = driver.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys('')

driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()

driver.implicitly_wait(10)
password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys('')
password.send_keys(Keys.ENTER)

driver.get(attendance_url)

driver.implicitly_wait(3)
last_name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input')
last_name.send_keys('')

first_name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
first_name.send_keys('')

choose_period = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[1]/span')
choose_period.click()

#fix so that it selects 4 instead of 3
click_period = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div[2]')
click_period.click()

#submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span')
#submit.click()
