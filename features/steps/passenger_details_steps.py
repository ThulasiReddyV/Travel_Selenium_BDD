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
from pages.bus_selection_page import Bus_Page
from pages. passenger_details_page import Passenger_Page

from utils.utilities import *
import logging

@when('user enter valid passenger details')

def passenger_details(context):
    data = context.test_data
    context.passenger = Passenger_Page(context.driver)

    context.passenger.trip_details()
    context.passenger.enter_mobile_no(data["pass_mobile"])
    context.passenger.enter_email(data["pass_email"])
    context.passenger.enter_name(data["pass_name"])
    context.passenger.enter_age(data["pass_age"])
    context.passenger.select_gender(data["pass_gender"])

    proceed_to_payment = context.passenger.continue_to_pay()
    if not proceed_to_payment:
        context.flow_stopped = True
        logging.info("Flow stopped — Due to Passenger Details not entered")
        return
        
    
    """context.passenger.verify_trip_details()
    context.passenger.generate_qr()"""




