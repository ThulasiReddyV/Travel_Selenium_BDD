from behave import *
#from selenium.webdriver import 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException

from pages.base_page import Base_Page


base_url = "https://www.abhibus.com/"


#driver= webdriver.Chrome()


@given('Give the url')
def go_to_url(context):
    #self.driver = driver
    context.base = Base_Page(context.driver)
    print("base")
    
    #raise StepNotImplementedError(u'Given Give the url')


@when('Enter the "{from_text}" and "{to_text}"')
def step_enterimpl(context,from_text,to_text):
    print("HI")
    
    context.base.enter_from(from_text)
    context.base.enter_to(to_text)
    #raise StepNotImplementedError(u'When enter the from and to')


@then('Land in the route details')
def step_impl(context):
    print("HI2")

    #raise StepNotImplementedError(u'Then Land in the route details')