# ref. https://github.com/RealTake/quasarzone_auto_daily_check

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AttChkBot:
    url_attendance = "https://quasarzone.com/users/attendance"

    def __init__(self, login_info):
        self.USER_ID = login_info['USER_ID']
        self.USER_PASSWORD = login_info['USER_PASSWORD_1']

    def att_check(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-notifications")
            options.add_argument("--safebrowsing-disable-download-protection")
            options.add_argument("--safebrowsing-disable-extension-blacklist")
            options.add_argument("--disable-extensions")
            driver = webdriver.Chrome('chromedriver', options=options)

            driver.get(self.url_attendance)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login_id"]'))).send_keys(
                self.USER_ID)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(
                self.USER_PASSWORD)
            time.sleep(2)
            driver.execute_script("document.querySelector('#frm > div > div.top-input-area > p > a').click()")
            driver.execute_script('anttendanceCheck()')
            driver.close()

            return True

        except:
            return False
