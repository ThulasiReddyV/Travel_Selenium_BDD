from selenium import webdriver
from pages.home_page import Home_Page
from pages.base_page import Base_Page

base_url = "https://www.abhibus.com/"

def before_scenario(context, scenario):
    #self.driver = driver
    context.driver = webdriver.Chrome()
    context.driver.get(base_url)
    context.driver.maximize_window()
    context.flow_stopped = False


    print("------------Before Scenario------------------")
    #print("Before Scenario")

def after_scenario(context, scenario):
    #self.driver = driver
    #print(context.base.past_date)

    #print("After Scenario")
    print("-------------After Scenario-----------------\n")

    """print(context.base.selected_date.date())
    print(context.base.today.date())
"""
    context.driver.quit()
    
