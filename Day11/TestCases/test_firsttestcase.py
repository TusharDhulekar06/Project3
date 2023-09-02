import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Test_firstcase:
    def test_firstcase(self):
        service=ChromeService(executable_path=ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)

        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)

        act_title=driver.title
        exp_title = "OrangeHRM"

        if act_title==exp_title:
            print("Login test pass")
        else:
            print("Login test failed ")
        driver.close()
