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
    #login
    driver.find_element(By.XPATH,"//a[contains(text(),'Account')]").click()
    print(driver.title)
    driver.find_element(By.XPATH,"//a[@class='ld-login ld-login ld-login-text ld-login-button ld-button']").click()
    driver.find_element(By.ID,"user_login").send_keys("root")
    driver.find_element(By.ID,"user_pass").send_keys("pa$$w0rd")
    driver.find_element(By.ID,"wp-submit").click()
    #all Cources
    driver.find_element(By.XPATH,"//a[contains(text(),'All Courses')]").click()
    print(driver.title)
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/main/article/div/section[2]/div[2]/div/div/div/div[2]/article/div[2]/p[2]/a").click()
    driver.find_element(By.XPATH,"//div[@id='ld-expand-91']").click()
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div/a/div[2]").click()










driver.quit()

#page_title = driver.title()
