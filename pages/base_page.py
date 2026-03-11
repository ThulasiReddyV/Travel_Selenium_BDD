from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException


from datetime import datetime
import time




class Base_Page:
    
    

    #NEXT_MONTH_BTN_CLASS = (By.CLASSNAME,"calender-month-change")

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.wait5 = WebDriverWait(driver,5)
        self.past_date = False
        self.max_date = False
        #self.flow_stopped = False
        
        
    def get_titile(self):
        return self.driver.title
    
    def get_url(self):
        return self.driver.current_url


    def dd_mm_yy_convert(self,departure_date):
        day, month,year = map(int, departure_date.split('/'))

        print(f"Given Date: {day}/{month}/{year}", end = "      ")
        return day,month,year

       
    