from selenium import webdriver


base_url = "https://www.abhibus.com/"

def before_scenario(context, scenario):
    #self.driver = driver
    context.driver = webdriver.Chrome()
    context.driver.get(base_url)
    context.driver.maximize_window()
    
    print("Before Scenario")

def after_scenario(context, scenario):
    #self.driver = driver
    print("After Scenario")

    context.driver.quit()
    
