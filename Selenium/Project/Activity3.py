from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:
    driver.get("https://alchemy.hguy.co/lms")
    text1 = driver.find_element(By.CSS_SELECTOR,"h3.uagb-ifb-title").text

    print(text1)

    if text1 == "Actionable Training":
        print("True")
    else:
        print("False")


    #page_title = driver.title()
