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
from utils.utilities import *
import logging

@when('user selects bus and seat for the valid date and route')
def bus_selection(context):
    data = context.test_data
    context.bus = Bus_Page(context.driver)

    
    if context.flow_stopped:
        logging.info("Flow stopped — skipping bus/seat selection")
        return
         
        
    proceed_to_buses_in_route = context.bus.total_available_buses()
        

    if not proceed_to_buses_in_route :
        context.flow_stopped = True
        logging.info("Flow stopped — no buses in route or date found")
        return
    
    proceed_to_select_bus = context.bus.tgsrtc_buses()
    if not proceed_to_select_bus :
        context.flow_stopped = True
        logging.info("Flow stopped - due to no service provider ")
        return  

    proceed_to_select_bp_dp_points = context.bus.bus_search(data["bus_ser_no"])
    if not proceed_to_select_bp_dp_points :
        context.flow_stopped = True
        logging.info("Flow stopped - due to no bus with the service number")

        return 
    
    proceed_to_select_seat = context.bus.board_drop_points(data["boarding_pt"],data["dropping_pt"])
    if not proceed_to_select_seat :
        context.flow_stopped = True
        logging.info("Flow stopped - due to Mutiple Boarding or Droping Points Loaded ")
        #logging.info("Flow stopped - due to selected seat already booked or on hold ")

        return
    
    proceed_to_enter_details = context.bus.seat_search(data["seat_no"])
    if not proceed_to_enter_details :
        context.flow_stopped = True
        logging.info("Flow stopped - due to Selected seat already booked ")
        #logging.info("Flow stopped - due to selected seat already booked or on hold ")

        return
    
    proceed_to_enter_details = context.bus.proceed_to_enter_details()
    