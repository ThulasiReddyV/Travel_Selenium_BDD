from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException


import datetime
import time



class Base_Page:
    
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    
    def dd_mm_yy_convert(self,departure_date):
        day, month,year = map(int, departure_date.split('/'))
        print( day, month,year)
        return day,month,year
       

