from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:
    driver.get("https://alchemy.hguy.co/lms")
    print(driver.title)
    #page_title = driver.title()
    if driver.title == "Alchemy LMS – An LMS Application":
        print("true")
    else:
        print("false")


