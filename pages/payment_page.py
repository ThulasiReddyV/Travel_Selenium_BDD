from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import Base_Page
from pages.home_page import Home_Page
from pages.bus_selection_page import Bus_Page
from pages.passenger_details_page import Passenger_Page


from datetime import datetime
import time
import logging

class Payment_Page(Passenger_Page):

    DETAILS_CSS=(By.CSS_SELECTOR,".mt-20.overflow-hidden.rounded-20.bg-common-white.pb-20.shadow-100")
    EXPAND_XPATH = (By.XPATH,".//*[contains(@class, 'transition-transform')]")
    CITIES_CSS = (By.CSS_SELECTOR," .body-md.font-medium")
    POINTS_TIME_CSS = (By.CSS_SELECTOR," .body-sm.text-secondary")
    #data-testid="ExpandMoreIcon"

    def verify_trip_details(self,data):
        
        try:
            details_ele = self.wait.until(EC.visibility_of_element_located(self.DETAILS_CSS))
            expand = details_ele.find_element(*self.EXPAND_XPATH)
            expand.click()
            logging.info("Expand clicked")
            time.sleep(1)
            logging.info(f"{details_ele.text} ")

            cities = details_ele.find_elements(*self.CITIES_CSS)
            page_from = cities[0].text
            page_to = cities[1].text

            points = details_ele.find_elements(*self.POINTS_TIME_CSS)
            page_boarding  = points[0].text
            page_dep_date  = points[1].text
            page_dropping  = points[2].text

            logging.info(f"From     : {page_from}")
            logging.info(f"To       : {page_to}")
            logging.info(f"Boarding : {page_boarding}")
            logging.info(f"Dropping : {page_dropping}")
            logging.info(f"Dep Date : {page_dep_date}")

            expected = {
                "From"     : (page_from,     data["from_loc"].capitalize()),
                "Boarding" : (page_boarding, data["boarding_pt"].capitalize()),
                "To"       : (page_to,       data["to_loc"].capitalize()),
                "Dropping" : (page_dropping, data["dropping_pt"].capitalize()),
                "Dep Date" : (page_dep_date, self.format_date(data["date_of_journey"])),
            }
            all_passed = True
            for field, (page_val, expected_val) in expected.items():
                if expected_val.lower() in page_val.lower():
                    logging.info(f"{field:12} | page: {page_val:20} | json: {expected_val}")
                else:
                    logging.info(f"{field:12} | page: {page_val:20} | json: {expected_val}")
                    all_passed = False

            return all_passed
        
        except TimeoutException:
            logging.info("Details not loaded")
            return False
            
    def generate_qr(self):
            
        generate_qr_ele = self.wait.until(EC.visibility_of_element_located(self.GENERATE_QR_BUTTON_XPATH))
        generate_qr_ele.click()
        time.sleep(10)
