Feature: Bus Seat Booking Validation
    Scenario Outline:  Validate the bus booking scenario in abhibus website
        Given load test data "<test_case_id>"
        When user select the date and routes search buses
        #And user selects bus and seat for the valid date and route
        #And user enter valid passenger details 
        Then Land in the payment page

    Examples:
    |   test_case_id    |
    |   Test_000 |
    |   Test_001 |
    |   Test_002 |
    """|   Test_003 |
    |   Test_004 |
    |   Test_005 |
    |   Test_006 |"""
    