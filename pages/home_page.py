from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException

from pages.base_page import Base_Page

from datetime import datetime, timedelta
import time



class Home_Page(Base_Page):

    FROM_TXT_XPATH = (By.XPATH,"//*[@placeholder = 'Leaving From']")
    TO_TXT_XPATH = (By.XPATH,"//*[@placeholder = 'Going To']")
    CLICK_1ST_SUGGESTION_LI_XPATH = (By.XPATH,"//li[@id='aci-option-0']//span[normalize-space()]")
    
    CALENDER_XPATH = (By.XPATH,"//*[@placeholder = 'Onward Journey Date']")
    SEARCH_BTN_XPATH = (By.XPATH,"//*[(@id = 'search-button') and (contains(@class , 'btn-search-wrapper'))]")
    NEXT_MONTH_BTN_XPATH = (By.XPATH,"//*[contains(@d, 'm9.4 17.1-.5-.5 4.6-4.6-4.6-4.6.5-.5 5.1 5.1Z')]/ancestor::span")
    
    
    """def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)"""

    def enter_from(self,from_loc):
        from_city = self.wait.until(EC.visibility_of_element_located(self.FROM_TXT_XPATH))
        from_city.click()
        from_city.clear()
        from_city.send_keys(from_loc)
        from_suggestion = self.wait.until(EC.element_to_be_clickable(self.CLICK_1ST_SUGGESTION_LI_XPATH))
        from_suggestion.click()
        print(from_city.get_attribute("value"))


    def enter_to(self,to_loc):
        to_city = self.wait.until(EC.visibility_of_element_located(self.TO_TXT_XPATH))
        to_city.click()
        to_city.clear()
        to_city.send_keys(to_loc)
        to_suggestion = self.wait.until(EC.element_to_be_clickable(self.CLICK_1ST_SUGGESTION_LI_XPATH))
        to_suggestion.click()
        print(to_city.get_attribute("value"))


            
    def select_date_of_journey(self,departure_date):
        
    
        
        calender = self.wait.until(EC.visibility_of_element_located(self.CALENDER_XPATH))
        calender.click()
        self.selected_date = datetime.strptime(departure_date, "%d/%m/%Y") 
        self.today = datetime.today()
        day,month,year = self.dd_mm_yy_convert(departure_date)
        
        if self.selected_date.date() < self.today.date():
            self.past_date = True
            print("Past Date")
            return False  
        
        elif self.selected_date.date() > self.today.date() + timedelta(days= 90):
            self.max_date = True
            print("Above 3 months Date")
            return False
        
        else:
            DATE_SELECT_XPATH = (By.XPATH,f'//*[@data-date="{day}" and @data-month="{month}" and @data-year="{year}"]')

            self.in_month(DATE_SELECT_XPATH)
            print(f"Selected Date: {calender.get_attribute("value")}")

            return True

      

    def in_month(self,DATE_SELECT_XPATH):    
        try:
            select_date = self.wait5.until(EC.visibility_of_element_located(DATE_SELECT_XPATH))
            select_date.click()
        except :
            self.next_month(DATE_SELECT_XPATH)

    def next_month(self,DATE_SELECT_XPATH):
        self.lastmonth_loaded = False

        try:
            nxt_month_btn = self.driver.find_element(*self.NEXT_MONTH_BTN_XPATH)
            nxt_month_btn.click()
            self.in_month(DATE_SELECT_XPATH)
        except NoSuchElementException:
            self.lastmonth_loaded = True
            print("Loaded upto Last Month ")


    def click_search(self):
        submit_btn = self.wait.until(EC.visibility_of_element_located(self.SEARCH_BTN_XPATH))
        submit_btn.click()
    