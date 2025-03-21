from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:
    driver.get("https://alchemy.hguy.co/lms")
    driver.find_element(By.XPATH,"//a[contains(text(),'Account')]").click()
    print(driver.title)





driver.quit()

#page_title = driver.title()
