from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException

from pages.base_page import Base_Page
from pages.home_page import Home_Page


from datetime import datetime
import time
import logging

class Bus_Page(Home_Page):
    
    
    TOTAL_SERVICES_IN_ROUTE_CLASS = (By.CLASS_NAME,"buses-availability")
    NO_SERVICES_MSG_ID = (By.ID,"not-found-container")
    TGSRTC_GROUP_ID = (By.ID,"group-service-TGSRTC")
    
    SERVICE_PROVIDER_NAME_CSS = (By.CSS_SELECTOR,".filter-name.text-neutral-800")
    SERVICE_PROVIDER_FULL_NAME_CSS = (By.CSS_SELECTOR,".fullName.text-truncate")
    TOTAL_SERVICES_BY_PROVIDER_CLASS = (By.CSS_SELECTOR,"span[class = 'text-truncate']")
    VIEW_BUSES = (By.XPATH,".//span[text()='View Buses']")

    BUS_SERVICE_ANCESTOR_XPATH = (By.XPATH,"./ancestor::div[contains(@class,'container') and contains(@id,'service-container')]")
    #FARE_INFO_XPATH = (By.XPATH,".//div[contains(@class,'fare-info') and contains(@id,'service-operator-fare-info')]")
    SEATS_INFO_XPATH = (By.XPATH,".//div[contains(@class,'seat-info') and contains(@id,'service-operator-select-seat')]")
    
    #row seat-info bd-success-400 text-success-500 bg-success-50
    #SELECT_SEATS_BUTTON_XPATH = (By.XPATH,".//button[contains(text() , 'Select Seats')]")
    SELECT_SEATS_BUTTON_XPATH = (By.XPATH,".//button")
    AVAILABLE_SEATS_XPATH = (By.XPATH,".//*[@class = 'svg-icon']")
    
    HIDE_SEATS = (By.XPATH,"//*[button[text()='Hide Seats']]")
    SELECT_BP_DP_TEXT = (By.XPATH,"//*[h6[text()='Select Boarding & Dropping point to continue']]")
    RADIO_BUTTON = (By.XPATH,"./ancestor::div[@class = ' col']")

    ALL_SEATS_CLASS = (By.CLASS_NAME, "Tooltip-Wrapper")
    BOOKED_SEATS_CSS = (By.XPATH, "//button[@class='seat']")
   
    #class="row collapsible-header  "


    def total_available_buses(self):

        try:
            
            total_buses_count = self.wait.until(EC.visibility_of_element_located(self.TOTAL_SERVICES_IN_ROUTE_CLASS))
            total_buses_count_msg = total_buses_count.text
            logging.info(f"{total_buses_count_msg}")
            return True
        except TimeoutException:
            try:
                no_services_ele = WebDriverWait(self.driver,2).until(EC.visibility_of_element_located(self.NO_SERVICES_MSG_ID))
                no_services_msg = no_services_ele.text
                logging.info(f"{no_services_msg}")
            except:
                logging.info("No service message not found either ")
        return False



        """#time.sleep(1.5)
        for i in range(50):
            try:
                total_buses_info = self.driver.find_element(*self.TOTAL_BUSES_MSG_CSS)
                msg = total_buses_info.text.replace("\n", "  ")
                logging.info(f"{msg}")
                return True

            except NoSuchElementException:
                time.sleep(0.1)
                continue
            
        try:
            no_services_ele = WebDriverWait(self.driver,2).until(EC.visibility_of_element_located(self.NO_SERVICES_MSG_ID))
            no_services_msg = no_services_ele.text
            logging.info(f"{no_services_msg}")
            return False    
        except:
            logging.info("No service message not found either ")
            return False """ 
    
    def tgsrtc_buses(self):
        
        try:
            self.bus_group_card = self.wait.until(EC.presence_of_element_located(self.TGSRTC_GROUP_ID))
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",self.bus_group_card)

            service_provider_name = self.bus_group_card.find_element(*self.SERVICE_PROVIDER_NAME_CSS)
            logging.info(f"{service_provider_name.text}")

            service_provider_full_name = self.bus_group_card.find_element(*self.SERVICE_PROVIDER_FULL_NAME_CSS)
            logging.info(f"{service_provider_full_name.text}")

            no_of_services_info = self.bus_group_card.find_element(*self.TOTAL_SERVICES_BY_PROVIDER_CLASS)
            logging.info(f"{no_of_services_info.text}")
            
            return  True
        except NoSuchElementException:

            logging.info(f"NO Service Provider with the name")
            return False
        
    def bus_search(self,service_no):

        #bus_group_card = self.driver.find_element(*self.TGSRTC_GROUP_ID)
        bus_group_card_expand = self.bus_group_card.find_element(*self.VIEW_BUSES)
        bus_group_card_expand.click()

        #logging.info(f" Service Provider with the name")
        BUS_WITH_SERVICE_NO_XPATH = (By.XPATH,f"//h5[contains(text() , '{service_no}')]")
        try:
            bus_element = self.wait.until(EC.visibility_of_element_located(BUS_WITH_SERVICE_NO_XPATH))
            logging.info(f"{bus_element.text}")

            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",bus_element)
            
            bus_container = bus_element.find_element(*self.BUS_SERVICE_ANCESTOR_XPATH)
            seats_info_container =  bus_container.find_element(*self.SEATS_INFO_XPATH)
            seats_info_msg = seats_info_container.text.replace ("\n"," -- ")
            logging.info(f"{seats_info_msg}")
            
            
            #available_seats_display = fare_info_container.find_element(*self.AVAILABLE_SEATS_XPATH)

            select_seats_btn = seats_info_container.find_element(*self.SELECT_SEATS_BUTTON_XPATH)

            select_seats_btn.click()
            return True
            
        except TimeoutException:

            logging.info(f"NO Service  with the Service number")
            return False
    
    def select_point(self,point):
        return (By.XPATH,f"//*[p[text()='{point.title()}']]")
         

    def board_drop_points(self,bp_point,dp_point):
        hide_seats_count = self.driver.find_elements(*self.HIDE_SEATS)

        if(len(hide_seats_count) == 1):
            bp_dp_point_text_element = self.wait.until(EC.visibility_of_element_located(self.SELECT_BP_DP_TEXT))

            bp_point_element = bp_dp_point_text_element.find_element(*self.select_point(bp_point))
            bp_loc = bp_point_element.find_element(*self.RADIO_BUTTON)
            logging.info(f"{bp_loc.text}")
            bp_loc.click()


            dp_point_element = bp_dp_point_text_element.find_element(*self.select_point(dp_point))
            dp_loc = dp_point_element.find_element(*self.RADIO_BUTTON)
            logging.info(f"{dp_loc.text}")
            dp_loc.click()

            return True
        else:
            return False

    def seat_search(self,seat_no):
        try:
            all_available_seats = self.wait.until(EC.presence_of_all_elements_located(self.ALL_SEATS_CLASS))
            logging.info(f"Total Available seats: {len(all_available_seats)}")

            """not_available_seats = self.wait.until(EC.presence_of_all_elements_located(self.BOOKED_SEATS_CSS))
            logging.info(f"Booked seats: {len(not_available_seats)}")"""

            """for no_seat in not_available_seats:
                # ── Read span without hovering ──
                number = self.driver.execute_script("return arguments[0].querySelector('span') ? arguments[0].querySelector('span').innerText : '';",no_seat)

                if number.strip() == str(seat_no).strip():
                    # ── Scroll to seat ──
                    self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", no_seat)
                    time.sleep(0.3)
                    logging.info(f"Seat {seat_no} not already booking ")
                    return False
            
            logging.info(f"Seat {seat_no} is available for booking")"""

            for seat in all_available_seats:
                # ── Read span without hovering ──
                number = self.driver.execute_script("return arguments[0].querySelector('span') ? arguments[0].querySelector('span').innerText : '';",seat)

                if number.strip() == str(seat_no).strip():
                    # ── Scroll to seat ──
                    self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", seat)
                    time.sleep(0.3)
                    seat.click()
                    logging.info(f"Seat {seat_no} selected ")
                    return True
            
            logging.info(f"Seat {seat_no}  already booking ")

            return False
            

        except TimeoutException:
            logging.info("Seats not loaded")
            return False
  

