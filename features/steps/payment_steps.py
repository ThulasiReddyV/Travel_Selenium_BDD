from behave import *
#from selenium.webdriver import 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException

from datetime import datetime
from pages.base_page import Base_Page
from pages.home_page import Home_Page
from utils.utilities import *

@then('Land in the payment page')

def validation(context):
    """context.base = Base_Page(context.driver)"""
    #context.base = Home_Page(context.driver)
    data = context.test_data
    check = context.base.get_url()
    if context.base.past_date == True :#and context.base.lastmonth_loaded == True  :
        assert context.flow_stopped == True, "Something went wrong"
    elif context.base.max_date == True:# and context.base.lastmonth_loaded == True :
        assert context.flow_stopped == True , "Something went wrong"
    else:
        print(check)
        assert data["from_loc"].lower() in check.lower() , "Website not"
        
