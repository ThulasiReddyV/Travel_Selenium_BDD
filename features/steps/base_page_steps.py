from behave import given,when,then
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
import logging
import time
#import functools
#print = functools.partial(print, flush=True)

#@given('load test data "{test_case_id}"')
@given('load test data "{test_case_id}"')
def load_test(context,test_case_id):
    
    context.test_data = read_and_get_json(test_case_id)
    test_id       = context.test_data["test_case_id"]   
    test_scenario = context.test_data["scenario"] 
    logging.info(f"TEST ID : {test_id}")
    logging.info(f"CENARIO : {test_scenario}")
    logging.info(f"{'='*60}")
    

@when('user select the date and routes search buses')

def entering_journey_details(context):
    logging.info("Select the date and routes")
    data = context.test_data
    context.base = Home_Page(context.driver)
    context.base.enter_from(data["from_loc"])
    context.base.enter_to(data["to_loc"])
    
    proceed = context.base.select_date_of_journey(data["date_of_journey"])
 
    logging.info(f"Given Date: {data['date_of_journey']}")
    logging.info(f"Proceed To Buses Page : {proceed}")
    #print(f"  Reason       : {reason}")
    if not proceed :
        context.flow_stopped = True
        logging.info("Past or max date")
    
    else:
        logging.info(f"Search clicked")
        context.base.click_search()
        context.buses_url = context.base.get_url()
    
    #raise StepNotImplementedError(u'When enter the from and to')


#@then('Land in the payment page')
def step_impl(context):
    context.base = Home_Page(context.driver)
    data = context.test_data
    check = context.base.get_url()
    logging.info(f"{check}")
    assert data["from_loc"].lower() in check.lower() , "Wrong Web"


    #raise StepNotImplementedError(u'Then Land in the route details')