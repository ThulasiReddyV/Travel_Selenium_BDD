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


from datetime import datetime
import time
import logging

class Passenger_Page(Home_Page):

    TRIP_DETAILS_XPATH = (By.XPATH,"//*[contains(@class,'trip-details-card-body')]")
    #MOBILE_NUM_INPUTMODE_XPATH = (By.XPATH,"//input[@inputmode='tel']")
    MOBILE_NUM_INPUTMODE_XPATH =  (By.XPATH,"//input[@placeholder='Mobile Number']")
    #EMAIL_TYPE_XPATH = (By.XPATH,"//input[@type='email']" )
    EMAIL_TYPE_XPATH = (By.XPATH,"//input[@placeholder='Email ID']")

    NAME_PLACEHOLDER_XPATH = (By.XPATH,"//input[@placeholder = 'Name']")
    AGE_PLACEHOLDER_XPATH = (By.XPATH,"//input[@placeholder = 'Age']")
    CONTINUE_TO_PAY_BUTTON_XPATH = (By.XPATH,"//a[contains(text(),'Continue to Pay')]")

    #CONTINUE_TO_PAY_XPATH = (By.XPATH,"//button[contains(text(),'Generate QR')]/..")
    GENERATE_QR_BUTTON_XPATH = (By.XPATH,"//button[contains(text(),'Generate QR')]")


    ERROR_CSS = (By.CSS_SELECTOR,".container.single-error-msg")

    DETAILS_CSS=(By.CSS_SELECTOR,".mt-20.overflow-hidden.rounded-20.bg-common-white.pb-20.shadow-100")
    EXPAND_XPATH = (By.XPATH,".//*[@class = 'transition-transform']")
    #data-testid="ExpandMoreIcon"
    
    def trip_details(self):
        trip_info = self.driver.find_element(*self.TRIP_DETAILS_XPATH)
        logging.info(f"{trip_info.text}")
        
    def enter_mobile_no(self,mobile_no):
        mobile_no_ele = self.wait.until(EC.visibility_of_element_located(self.MOBILE_NUM_INPUTMODE_XPATH))
        mobile_no_ele.click()
        mobile_no_ele.clear()
        mobile_no_ele.send_keys(mobile_no)
        logging.info(f"Mobile Number: {mobile_no_ele.get_attribute('value')}")

    def enter_email(self,email):
        email_ele = self.wait.until(EC.visibility_of_element_located(self.EMAIL_TYPE_XPATH))
        email_ele.click()
        email_ele.clear()
        email_ele.send_keys(email)
        logging.info(f"Email ID: {email_ele.get_attribute('value')}")


    def enter_name(self,name):
        name_ele = self.wait.until(EC.visibility_of_element_located(self.NAME_PLACEHOLDER_XPATH))
        name_ele.click()
        name_ele.clear()
        name_ele.send_keys(name)
        logging.info(f"Name: {name_ele.get_attribute('value')}")


    def enter_age(self,age):
        age_ele = self.wait.until(EC.visibility_of_element_located(self.AGE_PLACEHOLDER_XPATH))
        age_ele.click()
        age_ele.clear()
        age_ele.send_keys(age)
        logging.info(f"Age: {age_ele.get_attribute('value')}")


    def select_gender(self,gender):
        GENDER_XPATH = (By.XPATH,f"//button[text()='{gender.capitalize()}']")
        gender_ele = self.wait.until(EC.visibility_of_element_located(GENDER_XPATH))
        gender_ele.click()
        verify_gender_path = f".btn.btn-gender.{gender.lower()}.active.light.filled.primary.sm.rounded-md.inactive.button"
        logging.info(f"{verify_gender_path}")
        gender_verif = self.driver.find_elements(By.CSS_SELECTOR,verify_gender_path)
        if len(gender_verif) == 1:
            logging.info(f"Gender: {gender_verif[0].text}")


    def continue_to_pay(self):
        
        continue_btn_ele = self.wait.until(EC.visibility_of_element_located(self.CONTINUE_TO_PAY_BUTTON_XPATH))
        continue_btn_ele.click()

        error_ele = self.driver.find_elements(*self.ERROR_CSS)
        if (len(error_ele)>0):
            logging.info(f"Passenger Details not entered")
            self.passenger.not_entered = True
            return False
        return True
    
    def details(self):
        details_ele = self.wait.until(EC.visibility_of_element_located(self.DETAILS_CSS))
        expand = details_ele.find_element(*self.EXPAND_XPATH)
        expand.click()
        logging.info(f"{details_ele.text} ")
        
    def generate_qr(self):
        
        generate_qr_ele = self.wait.until(EC.visibility_of_element_located(self.GENERATE_QR_BUTTON_XPATH))
        generate_qr_ele.click()
