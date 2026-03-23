from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.home_page import Home_Page
from pages.base_page import Base_Page
import logging

import os
from datetime import datetime
#import functools
#print = functools.partial(print, flush=True)

# ── Create logs folder ──
os.makedirs("logs", exist_ok=True)

# ── File paths ──
timestamp   = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file    = os.path.join("logs", f"test_log_{timestamp}.txt")
latest_file = os.path.join("logs", "latest.txt")

# ── Root logger ──
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# ── Suppress noisy third party loggers ──
logging.getLogger("selenium").setLevel(logging.WARNING)   #  top level
logging.getLogger("urllib3").setLevel(logging.WARNING)    #  top level

# ── Formatter ──
formatter = logging.Formatter(
    "%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ── File handler — timestamped ──
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# ── File handler — latest.txt ──
latest_handler = logging.FileHandler(latest_file, mode="w", encoding="utf-8")
latest_handler.setLevel(logging.DEBUG)
latest_handler.setFormatter(formatter)
logger.addHandler(latest_handler)

# ── Console handler ──
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(
    "%(asctime)s  %(message)s",
    datefmt="%H:%M:%S"
))
logger.addHandler(console_handler)

base_url = "https://www.abhibus.com/"

def before_scenario(context, scenario):
     # ── Suppress Chrome/Selenium noisy logs ──
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])


    service = Service(log_path="NUL")  # Windows — throws chrome log to black hole

    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.get(base_url)
    context.driver.maximize_window()

    # ── Initialize context attributes ──
    context.flow_stopped = False
    #context.home         = None
    #context.stop_reason  = ""

    logging.info(f"\n{'='*60}")
    logging.info(f"  STARTING : {scenario.name}")
    logging.info(f"{'='*60}")
    

    #self.driver = driver
    """context.driver = webdriver.Chrome()
    context.driver.get(base_url)
    context.driver.maximize_window()
    context.flow_stopped = False


    print("------------Before Scenario------------------")"""
    #print("Before Scenario")

def after_scenario(context, scenario):

    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # ── Get from test data ──
    test_id       = context.test_data["test_case_id"]   
    test_scenario = context.test_data["scenario"]        
    clean_scenario = test_scenario.replace(" ", "_")     

    # ── Combine ──
    filename = f"screenshots/{test_id}_{clean_scenario}_{timestamp}.png"
    context.driver.save_screenshot(filename)
    logging.info(f"Screenshot saved: {filename}")
    logging.info(f"\n{'='*60}")
    logging.info(f"  FINISHED : {scenario.name}")
    logging.info(f"  STATUS   : {scenario.status}")
    logging.info(f"{'='*60}\n")
    #self.driver = driver
    #print(context.base.past_date)

    #print("After Scenario")
    #print("-------------After Scenario-----------------\n")

    """print(context.base.selected_date.date())
    print(context.base.today.date())
    """
    context.driver.quit()
    
