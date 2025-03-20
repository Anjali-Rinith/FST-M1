from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:
    driver.get("https://alchemy.hguy.co/lms")
    text1 = driver.find_element(By.XPATH,"//h3[contains(text(),'Email')]").text

    print(text1)

    if text1 == "Email Marketing Strategies":
        print("True")
    else:
        print("False")


driver.quit()

    #page_title = driver.title()
