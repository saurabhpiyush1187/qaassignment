Feature: Test WebApp
  As a QA
  I want to test WebApp
  So that I can verify devices in my network


  Scenario: Verify List of devices in my network
    When user sends get call to the devices
    Then User should get an OK response
    And the user should be returned with the list of devices with ip address


  Scenario: Verify Connection to a device
    Given user is disconnected from all devices
    Then the user should be able to connect to one of the devices
    And the user should not be able to connect to another device
    When the current device is disconnected
    Then the user should be able to connect to another device


  Scenario: Verify State of a device
    Given user is disconnected from all devices
    Then the user should be able to connect to one of the devices
    And the user should be able to get the state of the connected device

  Scenario Outline: Verify State of a device when disconnected from the device
    Given user is disconnected from all devices
    Then the user should not be able to get the state of the device
    And the user should not be able to change the <property> of the device with the <value>
    Examples:
      | property   | value |
      | brightness | 5     |
      | color      | #ff000|
      | name       | eureka|



  Scenario Outline: Change name of the device-true
    Given user is disconnected from all devices
    Then the user should be able to connect to one of the devices
    And the user should be able to get the state of the connected device
    When the user changes the <name> of the device
    Then the response should be <result>
    And the user should be able to get the state of the connected device
    And the <name> should reflect in the state of the device
    Examples:
      | name     | result             |
      | bulb56   | {"success": True}  |


  Scenario Outline: Change name of the device-false
    Given user is disconnected from all devices
    Then the user should be able to connect to one of the devices
    And the user should be able to get the state of the connected device
    When the user changes the <name> of the device
    Then the response should be <result>
    And the user should be able to get the state of the connected device
    And the <name> should not reflect in the state of the device
    Examples:
      | name     | result             |
      |          | {"success": False} |
      | 67888    | {"success": False} |
      | -1       | {"success": False} |
      | %^&*%^*% | {"success": False} |


  Scenario Outline: Change brightness of the device-true
    Given user is disconnected from all devices
    Then the user should be able to connect to one of the devices
    And the user should be able to get the state of the connected device
    When the user changes the <brightness> of the device
    Then the response should be <result>
    And the user should be able to get the state of the connected device
    And the <brightness> should reflect in the state of the device
    Examples:
      | brightness | result            |
      | 0          | {"success": True} |
      | 10         | {"success": True} |
      | 5          | {"success": True} |



  Scenario Outline: Change brightness of the device- false
    Given user is disconnected from all devices
    Then the user should be able to connect to one of the devices
    And the user should be able to get the state of the connected device
    When the user changes the <brightness> of the device
    Then the response should be <result>
    And the user should be able to get the state of the connected device
    And the <brightness> should not reflect in the state of the device
    Examples:
      | brightness | result             |
      | 11         | {"success": False} |
      | a          | {"success": False} |
      | -1         | {"success": False} |
      |            | {"success": False} |
      | %^&*%^*%   | {"success": False} |


  Scenario Outline: Change color of the device - true
    Given user is disconnected from all devices
    Then the user should be able to connect to one of the devices
    And the user should be able to get the state of the connected device
    When the user changes the <color> of the device
    Then the response should be <result>
    And the user should be able to get the state of the connected device
    And the <color> should reflect in the state of the device
    Examples:
      | color    | result             |
      | #ff0000   | {"success": True}  |


  Scenario Outline: Change color of the device - false
    Given user is disconnected from all devices
    Then the user should be able to connect to one of the devices
    And the user should be able to get the state of the connected device
    When the user changes the <color> of the device
    Then the response should be <result>
    And the user should be able to get the state of the connected device
    And the <color> should not reflect in the state of the device
    Examples:
      | color    | result             |
      | 0000     | {"success": False} |
      | a        | {"success": False} |
      | 10       | {"success": False} |
      |          | {"success": False} |
      | %^&*%^*% | {"success": False} |

  Scenario: Change brightness back to 10
    Given user is disconnected from all devices
    Then the user should be able to connect to one of the devices
    And the user should be able to get the state of the connected device
    When the user changes the brightness to "5"
    Then the changed brightness5 should be reflected in the state
    When the user changes the brightness to "10"
    Then the changed brightness10 should be reflected in the state

  Scenario Outline: Store property after re-connecting to the device
    Given user is disconnected from all devices
    Then the user should be able to connect to one of the devices
    When the user changes the <color> of the device
    And the user changes the <brightness> of the device
    And the user changes the <name> of the device
    Then the user should be able to get the state of the connected device
    When the user disconnect the device and re-connect again to the same device
    Then the user should be able to see the changes in the connected device

    Examples:
      | color    | brightness            | name       |
      | ff0000   | 5                     |Bulb_newname|
