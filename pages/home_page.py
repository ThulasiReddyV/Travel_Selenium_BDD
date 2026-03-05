from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException

from pages.base_page import Base_Page

import datetime
import time



class Home_Page(Base_Page):

    FROM_TXT_XPATH = (By.XPATH,"//*[@placeholder = 'Leaving From']")
    FROM_SUGGESTION_XPATH = (By.XPATH,"//*[span[text()='Hyderabad'] and small[text()='(All boarding points)']]")
    TO_TXT_XPATH = (By.XPATH,"//*[@placeholder = 'Going To']")

    TO_SUGGESTION_XPATH = (By.XPATH,"//*[span[text()='Tirupati'] and small[text()='(All drop points)']]")
    CALENDER_XPATH = (By.XPATH,"//*[@placeholder = 'Onward Journey Date']")
    NEXT_MONTH_BTN_CLASS = (By.CLASS_NAME,"calender-month-change")
    SEARCH_BTN_XPATH = (By.XPATH,"//*[(@id = 'search-button') and (contains(@class , 'btn-search-wrapper'))]")

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


    def select_date_of_journey(self,departure_date):
        calender = self.wait.until(EC.visibility_of_element_located(self.CALENDER_XPATH))
        calender.click()
        day, month,year = self.dd_mm_yy_convert(departure_date)
        DATE_SELECT_XPATH = (By.XPATH,f'//*[@data-date="{day}" and @data-month="{month}" and @data-year="{year}"]')

        select_date = self.wait.until(EC.visibility_of_element_located(DATE_SELECT_XPATH))
        select_date.click()

    def click_search(self):
        submit_btn = self.wait.until(EC.visibility_of_element_located(self.SEARCH_BTN_XPATH))
        submit_btn.click()
    