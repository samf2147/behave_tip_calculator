Feature: Confirming that the tip calculator form displays

    Scenario: check that the form displays
        When I go to the tip calculator
        Then I should see the calculator form
    
    Scenario: check that the form submits successfully
        When I go to the tip calculator
        And I submit the form with a valid total and tip percentage
        Then I should see the results page
        And the results are accurate