from behave import *
#from selenium.webdriver import 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException

from pages.base_page import Base_Page
from pages.home_page import Home_Page
from utils.utilities import *


@given('load test data "{test_case_id}"')
def load_test(context,test_case_id):
    
    context.test_data = read_and_get_json(test_case_id)
    

@when('user select the date and routes search buses')

def entering_journey_details(context):
    print("Select the date and routes")
    data = context.test_data
    context.base = Home_Page(context.driver)
    context.base.enter_from(data["from_loc"])
    context.base.enter_to(data["to_loc"])
    
    proceed = context.base.select_date_of_journey(data["date_of_journey"])
    """
    print(f"Given Date  : {data['date_of_journey']}")
    print("Proceed      : ",proceed)
    #print(f"  Reason       : {reason}")"""
    if not proceed :
        context.flow_stopped = True
        print("PASt or max date")
    
    else:
        context.base.click_search()
    
    #raise StepNotImplementedError(u'When enter the from and to')


#@then('Land in the payment page')
def step_impl(context):
    context.base = Home_Page(context.driver)
    data = context.test_data
    check = context.base.get_url()
    print(check)
    assert data["from_loc"].lower() in check.lower() , "Wrong Web"


    #raise StepNotImplementedError(u'Then Land in the route details')