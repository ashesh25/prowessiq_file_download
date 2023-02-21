Feature: Test Login Feature

  #Background:
    #Given Launch URL




  @001
  Scenario Outline: Login to applicatin
    Given Launch URL
    Given Verify the Login Page title
    Then user enters username as "<username>"
    And password as "<password>"
    And hits the login button
    Then Verify Login was successful
  Examples:
    |username|password|
    |||

  @001
  Scenario Outline: user downloads data
    Then user search with company "<CompanyName>"
    And user creates local folder with name "<FolderName>"
    Then user downloads all the documents
    Then user clear all the previous file from "<FolderName>"
    And Moves all files from download to "<FolderName>"
    Examples:
      |CompanyName|FolderName|
      |Infosys Ltd.|Infosys|
      |Tata Consultancy Services Ltd.|TCS|
      |HOUSING DEVELOPMENT FINANCE CORPN. LTD.|HDFC|

  @002
  Scenario Outline: Verify user is able to login Successfully
    Given Verify the Login Page title
    Then user enters username as "<username>"
    And password as "<password>"
    And hits the login button
    Then Verify Login was successful
    Then user search with company "<CompanyName>"
    And user creates local folder with name "<FolderName>"
    Then user downloads all the documents
    Then user clear all the previous file from "<FolderName>"
    And Moves all files from download to "<FolderName>"
    Then user logs out of the application

    Examples:
    |username|password|CompanyName|FolderName|
    |||Infosys Ltd.|Infosys|
    |||Tata Consultancy Services Ltd.|TCS|