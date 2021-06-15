from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path = "/Users/eliran/Documents/etudes/Python exercices/selenium/chromedriver")
#driver.maximize_window()
driver.get("https://www.google.com/")
driver.implicitly_wait(5)

#recherche google
search_input = driver.find_element(By.NAME,"q").send_keys("rocket espresso milano")
search_input = driver.find_element(By.CLASS_NAME,"gNO89b").click()
time.sleep(0.5)
site = driver.find_element(By.CLASS_NAME,"LC20lb").click()
time.sleep(2)

#menu domestics models --> appartamento
domestics = driver.find_element(By.ID,"u111764")
appartamento = driver.find_element(By.ID,"u111778-2")
action = ActionChains(driver)
action.move_to_element(domestics).move_to_element(appartamento).click().perform()

#data espreso machine
first_title = driver.find_element(By.ID,"u30136-2")
paragraphe = driver.find_element(By.XPATH,"//*[@id='u30136-19']/p[1]")
second_paragraphe = driver.find_element(By.XPATH,"//*[@id='u30136-19']/p[2]")

all_title = [first_title.text, paragraphe.text, second_paragraphe.text]

for titles in all_title:
    print(titles)



print("test completed")
time.sleep(2)
driver.quit()