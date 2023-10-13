# Created by balamurugann at 10/13/23
Feature: User can open Subscription & payments page in Reelly webpage

  Scenario: User can open Subscription & payments page
    Given Open the login page
    When Login to the page
    Then Click on settings option
    Then Click on Subscription And payments option
    Then Verify the Subscription & payments page opens and visible
    Then Verify title of Subscription & payments is visible
     And Verify <- Back button back are available
     And Verify Upgrade plan are available
