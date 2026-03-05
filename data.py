base_url = "https://www.abhibus.com/"
FROM_XPATH = (By.XPATH,"//div[text() = 'Leaving From']")
FROM_SUGGESTION_XPATH = (By.XPATH,"//*[span[text()='Hyderabad'] and small[text()='(All boarding points)']]")

TO_XPATH = (By.XPATH,"//div[text() = 'Going To']")
TO_SUGGESTION_XPATH = (By.XPATH,"//*[span[text()='Tirupati'] and small[text()='(All drop points)']]")

CALENDER_XPATH = (By.XPATH,"//*[@placeholder = 'Onward Journey Date']")
NEXT_MONTH_BTN_CLASS = (By.CLASSNAME,"calender-month-change")

day, month,year = map(int, "02/04/2026".split('/'))
print( day, month,year)  # Output: 2 4 2026

DATE_SELECT_XPATH = (By.XPATH,'//*[@data-date="{day}" and @data-month="{month}" and @data-year="{year}"]')
SEARCH_XPATH = (By.XPATH,"//*[(@id = 'search-button') and (contains(@class , 'btn-search-wrapper'))]")

ERROR_CLASS = (By.CLASSNAME,"error")

ORIGIN_ERR = "Please enter your Origin City"
DES_ERR = "Please enter your Destination City"
NO_SERVICES_MSG_ID = (By.ID,"not-found-container")
TGSRTC_ID = (By.ID,"group-service-TGSRTC")
TGSRTC_OPEN_XPATH = (By.XPATH,"//*[@id='group-service-TGSRTC']/div")
SEATS_INFO_XPATH_WITH_PARENT = (By.XPATH,"//*[contains(@class,'text-truncate')]")
BUS_WITH_SERVICE_NO_XPATH = (By.XPATH,"//h5[contains(text() , '{service_no}')]")
BUS_SERVICE_ANCESTOR_XPATH = (By.XPATH,"./ancestor::div[contains(@class,'container') and contains(@id,'service-container')]")
SELECT_SEATS_BUTTON_CHILD_XPATH = (By.XPATH,".//button[contains(text() , 'Select Seats')]")
//h5[contains(text() , '1759')]/ancestor::div[contains(@class,'container')and contains(@class,'rounded-md') and contains(@id,'service')]
//button[contains(text() , 'Select Seats')]
//p[contains(text() , 'Ecil X Road')]
//p[contains(text() , 'Tirupati Bs')]

BOARDING_POINT_SELECT_CHILD_XPATH = (By.XPATH,".//p[contains(text() , '{Boarding_point}')]/../../preceding-sibling::span [@class= 'radio-indicator']")
DROPPING_POINT_SELECT_CHILD_XPATH = (By.XPATH,".//p[contains(text() , '{Dropping_point}')]/../../preceding-sibling::span [@class= 'radio-indicator']")
SEAT_WRAPPER_CLASS = (By.CLASSNAME,"Tooltip-Wrapper ")
SEAT_NO_SEARCH_XPATH= (By.XPATH,".//span[text()='35']")
SEAT_SELECT_XPATH = (By.XPATH,"//span[text()='35']/ancestor:: div[contains(@class, 'Tooltip-Tip')]/preceding-sibling::button [@class= 'seat']")

SKIP_LOGIN_XPATH = (By.XPATH,"//a[text()='Skip']")

TRIP_DETAILS_XPATH = (By.XPATH,"//*[contains(@class,'trip-details-card-body')]")
MOBILE_NUM_INPUTMODE_XPATH = (By.XPATH,"//input[@inputmode='tel']"  or "//input[@placeholder='Mobile Number']")
EMAIL_TYPE_XPATH = (By.XPATH,"//input[@type='email']" or "//input[@placeholder='Email ID']")
NAME_PLACEHOLDER_XPATH = (By.XPATH,"//input[@placeholder = 'Name']")
AGE_PLACEHOLDER_XPATH = (By.XPATH,"//input[@placeholder = 'Age']")
GENDER_XPATH = (By.XPATH,"//button[text()='Male']")
CONTINUE_TO_PAY_XPATH = (By.XPATH,,"//a[contains(text(),'Continue to Pay')]")
CONTINUE_TO_PAY_BUTTON_XPATH = (By.XPATH,"//button[contains(text(),'Generate QR')]")
CONTINUE_TO_PAY_XPATH = (By.XPATH,"//button[contains(text(),'Generate QR')]/..")


//h5[contains(text() , '1759')]/ancestor::div[contains(@class,'container')and contains(@class,'rounded-md') and contains(@id,'service')]//p[contains(text() , 'Mgbs')]
/preceding-sibling::span [@class= 'radio-indicator']
class Tooltip-Tip top dark
class="Tooltip-Wrapper "

//h5[contains(text() , '1777')]/ancestor::div[contains(@class,'container')and contains(@class,'rounded-md') and contains(@id,'service')]//span[text()='35']/ancestor:: div[contains(@class, 'Tooltip-Tip')]/preceding-sibling::button [@class= 'seat']

//h5[contains(text() , '1777')]/ancestor::div[contains(@class,'container')and contains(@class,'rounded-md') and contains(@id,'service')]//button[contains(text(),"Proceed")]


//*[contains(@class,"container") and contains(@class,"error")]

class mt-20 overflow-hidden rounded-20 bg-common-white pb-20 shadow-100