# example.feature
Feature: An example of behavior driven design

Scenario: I want to subtract two integers
Given our subtractor is installed
When I subtract 4 from 7
Then the result should be 3

Scenario: I want subtract floats
Given our subtractor is installed
When I subtract 3.5 from 7.0
Then it should return 3.5 within 0.0001 error
