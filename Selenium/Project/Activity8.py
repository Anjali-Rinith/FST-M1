import time

from selenium import webdriver
#from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:
    driver.get("https://alchemy.hguy.co/lms")
    driver.find_element(By.XPATH,"//a[contains(text(),'Contact')]").click()
    print(driver.title)
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='wpforms-8-field_0']").send_keys("AkhyaK")
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='wpforms-8-field_1']").send_keys("akhykris@in.ibm.com")
    driver.find_element(By.XPATH,"//input[@id='wpforms-8-field_3']").send_keys("FST")
    time.sleep(6)
    driver.find_element(By.XPATH,"//textarea[@id='wpforms-8-field_2']").send_keys("none")
    time.sleep(4)
    driver.find_element(By.XPATH,"//button[@id='wpforms-submit-8']").click()

    print(driver.find_element(By.ID,"wpforms-confirmation-8").text)



driver.quit()

#page_title = driver.title()
