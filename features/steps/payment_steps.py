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
from pages.bus_selection_page import Bus_Page
from pages.passenger_details_page import Passenger_Page
from pages.payment_page import Payment_Page
from utils.utilities import *
import logging
import time


@then('Land in the payment page')
def validation(context):
    data = context.test_data

    context.base = Base_Page(context.driver)
    context.home = Home_Page(context.driver)
   
    if context.home.past_date:
        assert context.flow_stopped, "FAIL: Past date"
        logging.info("PASS — Past date blocked")
        return

    elif context.home.max_date:
        assert context.flow_stopped, "FAIL: Max date"
        logging.info("PASS — Max date blocked")
        return

    elif context.flow_stopped:
        assert context.flow_stopped, "FAIL: flow stopped"
        logging.info("PASS — flow stopped correctly")
        return

    
    
    assert data["from_loc"].lower() in context.buses_url.lower(), "FAIL: Wrong page loaded"
    logging.info(f"URL correct ")

    

    assert "passengerinfo" in context.passenger_url.lower(), "FAIL: Passenger info page not loaded"
    logging.info("Passenger info page loaded")

    context.passenger = Passenger_Page(context.driver)
    context.payment   = Payment_Page(context.driver)

    if context.flow_stopped:
        assert context.flow_stopped, "FAIL: Passenger details not entered"
        logging.info("PASS — Passenger details not entered")
        return

    time.sleep(3)
    context.payment_url = context.base.get_url()
    assert "payments" in context.payment_url.lower(), "FAIL: Payment page not loaded"
    logging.info("Payment page loaded")

    assert context.payment.verify_trip_details(data), "FAIL: Trip details mismatch!"
    logging.info("All trip details verified")

    
    context.payment.generate_qr()
    logging.info("QR generated")
        
        
        
