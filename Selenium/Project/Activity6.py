from selenium import webdriver
#from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:
    driver.get("https://alchemy.hguy.co/lms")
    driver.find_element(By.XPATH,"//a[contains(text(),'Account')]").click()
    print(driver.title)
    driver.find_element(By.XPATH,"//a[@class='ld-login ld-login ld-login-text ld-login-button ld-button']").click()
    driver.find_element(By.ID,"user_login").send_keys("root")
    driver.find_element(By.ID,"user_pass").send_keys("pa$$w0rd")
    driver.find_element(By.ID,"wp-submit").click()
    text1 = driver.find_element(By.XPATH,"//a[@class='ld-logout ld-logout ld-login-text ld-login-button ld-button']").text

    if text1.upper() == 'LOGOUT':
        print("logged in")
    else:
        print("not logged in")








driver.quit()

#page_title = driver.title()
