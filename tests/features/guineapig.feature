Feature: Manipulating the guinea pig test website

  Scenario Outline: We want to check the first box
    Given we are looking at the guinea pig website
    When we click on the uncheck box
    Then it should be checked


