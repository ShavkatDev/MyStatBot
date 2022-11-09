from encodings import utf_8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Куки не работают на этом инвалидном сайте
import pickle

import config
import time


def getHtml():
    try:
        url = "https://mystat.itstep.org/ru/auth/login/index"

        # Если нужен рандомный user-agent
        # useragent = UserAgent()

        # option = webdriver.ChromeOptions()
        # option.add_argument(f"user-agent={useragent.random}")

        # driver
        # Сюда путь до драйвера
        driver = webdriver.Chrome(
            executable_path=r"C:\Users\aliex\Desktop\Coding\projects\myStat_telegramBot.py\virtualVenvSelenium\chromedriver\chromedriver.exe")
        driver.get(url=url)
        time.sleep(4)

        loginInput = driver.find_element(By.ID, "username")
        passwordInput = driver.find_element(By.ID, "password")
        loginInput.clear()
        loginInput.send_keys(config.login)
        passwordInput.clear()
        passwordInput.send_keys(config.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)

        with open("index.html", "w", encoding="utf_8") as htmlPage:
            htmlPage.write(driver.page_source)

        driver.close()
        driver.quit()

    except Exception as ex:
        print(ex)

    finally:
        print("Driver is Done")
