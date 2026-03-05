from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException


import datetime
import time



class Base_Page:

    FROM_TXT_XPATH = (By.XPATH,"//*[@placeholder = 'Leaving From']")
    FROM_SUGGESTION_XPATH = (By.XPATH,"//*[span[text()='Hyderabad'] and small[text()='(All boarding points)']]")
    TO_TXT_XPATH = (By.XPATH,"//*[@placeholder = 'Going To']")

    TO_SUGGESTION_XPATH = (By.XPATH,"//*[span[text()='Tirupati'] and small[text()='(All drop points)']]")
    CALENDER = (By.XPATH,"//*[@placeholder = 'Onward Journey Date']")
    NEXT_MONTH_BTN_CLASS = (By.CLASS_NAME,"calender-month-change")

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def enter_from(self,from_loc):
        from_city = self.wait.until(EC.visibility_of_element_located(self.FROM_TXT_XPATH))
        from_city.click()
        from_city.clear()
        from_city.send_keys(from_loc)
        from_suggestion =  self.wait.until(EC.element_to_be_clickable(self.FROM_SUGGESTION_XPATH))
        from_suggestion.click()


    def enter_to(self,to_loc):
        to_city = self.wait.until(EC.visibility_of_element_located(self.TO_TXT_XPATH))
        to_city.click()
        to_city.clear()
        to_city.send_keys(to_loc)
        to_suggestion =  self.wait.until(EC.element_to_be_clickable(self.TO_SUGGESTION_XPATH))
        to_suggestion.click()