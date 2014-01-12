Feature: Confirming that the tip calculator form displays

    Scenario: check that the form displays
        When I go to the tip calculator
        Then I should see the calculator form
    
    Scenario: check that the form submits successfully
        When I go to the tip calculator
        And I submit the form with a valid total and tip percentage
        Then I should see the results page
        And the results are accurate
    
    Scenario: check negative total
        When I go to the tip calculator
        And I submit the form with a negative total
        Then I should see an error page
    
    Scenario: check negative tip
        When I go to the tip calculator
        And I submit the form with a negative tip
        Then I should see an error page
    
    Scenario: check non-integer inputs
        When I go to the tip calculator
        And I submit the form with non-integer total and tip
        Then I should see my answer rounded to two decimal places
    