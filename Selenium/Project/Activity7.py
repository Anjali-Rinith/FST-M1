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

    #all Cources
    driver.find_element(By.XPATH,"//a[contains(text(),'All Courses')]").click()
    print(driver.title)
    time.sleep(2)
    lists1 = driver.find_elements(By.XPATH,"//div[@class='ld-course-list-items row']/*")


    print("Number of courses",len(lists1))








driver.quit()

#page_title = driver.title()
