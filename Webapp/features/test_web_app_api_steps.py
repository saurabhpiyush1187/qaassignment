from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)
import os
from features.services.WebApp.web_app_api import WebApp
web_app = WebApp()



@scenario(r'tests' + os.sep + 'webapp'  + os.sep + 'web_app_api.feature', 'Verify List of devices in my network')
def test_verify_list_of_devices_in_my_network():
    """Verify List of devices in my network."""

@scenario(r'tests' + os.sep + 'webapp'  + os.sep + 'web_app_api.feature', 'Change brightness back to 10')
def test_change_brightness_back_to_10():
    """Change brightness back to 10."""


@scenario(r'tests' + os.sep + 'webapp'  + os.sep + 'web_app_api.feature', 'Change brightness of the device- false')
def test_change_brightness_of_the_device_false():
    """Change brightness of the device- false."""


@scenario(r'tests' + os.sep + 'webapp'  + os.sep + 'web_app_api.feature', 'Change brightness of the device-true')
def test_change_brightness_of_the_devicetrue():
    """Change brightness of the device-true."""


@scenario(r'tests' + os.sep + 'webapp'  + os.sep + 'web_app_api.feature', 'Change color of the device - false')
def test_change_color_of_the_device__false():
    """Change color of the device - false."""


@scenario(r'tests' + os.sep + 'webapp'  + os.sep + 'web_app_api.feature', 'Change color of the device - true')
def test_change_color_of_the_device__true():
    """Change color of the device - true."""


@scenario(r'tests' + os.sep + 'webapp'  + os.sep + 'web_app_api.feature', 'Change name of the device-false')
def test_change_name_of_the_devicefalse():
    """Change name of the device-false."""


@scenario(r'tests' + os.sep + 'webapp'  + os.sep + 'web_app_api.feature', 'Change name of the device-true')
def test_change_name_of_the_devicetrue():
    """Change name of the device-true."""


@scenario(r'tests' + os.sep + 'webapp'  + os.sep + 'web_app_api.feature', 'Store property after re-connecting to the device')
def test_store_property_after_reconnecting_to_the_device():
    """Store property after re-connecting to the device."""


@scenario(r'tests' + os.sep + 'webapp'  + os.sep + 'web_app_api.feature', 'Verify Connection to a device')
def test_verify_connection_to_a_device():
    """Verify Connection to a device."""



@scenario(r'tests' + os.sep + 'webapp'  + os.sep + 'web_app_api.feature', 'Verify State of a device')
def test_verify_state_of_a_device():
    """Verify State of a device."""


@scenario(r'tests' + os.sep + 'webapp'  + os.sep + 'web_app_api.feature', 'Verify State of a device when disconnected from the device')
def test_verify_state_of_a_device_when_disconnected_from_the_device():
    """Verify State of a device when disconnected from the device."""

    
@when('user sends get call to the devices')
def user_sends_get_call_to_the_devices():
    """user sends get call to the devices."""
    web_app.list_devices()


@then('User should get an OK response')
def user_should_get_an_ok_response():
    """User should get an OK response."""
    assert web_app.validate_reponse()


@then('the user should be returned with the list of devices with ip address')
def the_user_should_be_returned_with_the_list_of_devices_with_ip_address():
    """the user should be returned with the list of devices with ip address."""
    assert web_app.validate_list_devices()


@given('user is disconnected from all devices')
def user_is_disconnected_from_all_devices():
    """user is disconnected from all devices."""
    assert web_app.disconnect_from_device()


@when('the current device is disconnected')
def the_current_device_is_disconnected():
    """the current device is disconnected."""
    assert  web_app.disconnect_from_device()


@when('the user changes the <brightness> of the device')
def the_user_changes_the_brightness_of_the_device(brightness):
    """the user changes the <brightness> of the device."""
    web_app.change_property_softassert("brightness",brightness)


@when('the user changes the <color> of the device')
def the_user_changes_the_color_of_the_device(color):
    """the user changes the <color> of the device."""
    web_app.change_property_softassert("color",color)


@when('the user changes the <name> of the device')
def the_user_changes_the_name_of_the_device(name):
    """the user changes the <name> of the device."""
    web_app.change_property_softassert("name",name)



@when(parsers.cfparse('the user changes the brightness to "{n}"'))
def the_user_changes_the_brightness_to(n):
    """the user changes the brightness to "5"."""
    print("Changing brightness to "+ str(n) +"...")
    web_app.change_property_softassert("brightness",n)


@when('the user disconnect the device and re-connect again to the same device')
def the_user_disconnect_the_device_and_reconnect_again_to_the_same_device():
    """the user disconnect the device and re-connect again to the same device."""
    assert web_app.disconnect_from_device()
    assert web_app.connect_to_device1()




@then('the <name> should not reflect in the state of the device')
def the_name_should_not_reflect_in_the_state_of_the_device(name):
    """the <name> should not reflect in the state of the device."""
    assert (web_app.check_value_in_state("name",name),False)


@then('the <name> should reflect in the state of the device')
def the_name_should_reflect_in_the_state_of_the_device(name):
    """the <name> should reflect in the state of the device."""
    assert web_app.check_value_in_state("name",name)

@then('the <brightness> should not reflect in the state of the device')
def the_name_should_not_reflect_in_the_state_of_the_device(brightness):
    """the <name> should not reflect in the state of the device."""
    assert (web_app.check_value_in_state("brightness",brightness),False)


@then('the <brightness> should reflect in the state of the device')
def the_name_should_reflect_in_the_state_of_the_device(brightness):
    """the <name> should reflect in the state of the device."""
    assert web_app.check_value_in_state("brightness",brightness)


@then('the <color> should not reflect in the state of the device')
def the_name_should_not_reflect_in_the_state_of_the_device(color):
    """the <name> should not reflect in the state of the device."""
    assert (web_app.check_value_in_state("color",color),False)


@then('the <color> should reflect in the state of the device')
def the_name_should_reflect_in_the_state_of_the_device(color):
    """the <name> should reflect in the state of the device."""
    assert web_app.check_value_in_state("color",color)


@then('the changed brightness5 should be reflected in the state')
def the_changed_brightness_should_be_reflected_in_the_state_5():
    """the changed brightness should be reflected in the state."""
    assert web_app.get_state()
    assert web_app.check_value_in_state("brightness","5")

@then('the changed brightness10 should be reflected in the state')
def the_changed_brightness_should_be_reflected_in_the_state_10():
    """the changed brightness should be reflected in the state."""
    assert web_app.get_state()
    assert web_app.check_value_in_state("brightness","10")


@then('the response should be <result>')
def the_response_should_be_result(result):
    """the response should be <result>."""
    assert web_app.check_response(result)


@then('the user should be able to connect to another device')
def the_user_should_be_able_to_connect_to_another_device():
    """the user should be able to connect to another device."""
    assert web_app.connect_to_device2()


@then('the user should be able to connect to one of the devices')
def the_user_should_be_able_to_connect_to_one_of_the_devices():
    """the user should be able to connect to one of the devices."""
    assert web_app.connect_to_device1()


@then('the user should be able to get the state of the connected device')
def the_user_should_be_able_to_get_the_state_of_the_connected_device():
    """the user should be able to get the state of the connected device."""
    assert web_app.get_state()


@then('the user should be able to see the changes in the connected device')
def the_user_should_be_able_to_see_the_changes_in_the_connected_device():
    """the user should be able to see the changes in the connected device."""
    assert web_app.check_value_after_reconnect()




@then('the user should not be able to change the <property> of the device with the <value>')
def the_user_should_not_be_able_to_change_the_property_of_the_device(property,value):
    """the user should not be able to change the <property> of the device."""
    print("Trying to change property with device disconnected")
    bln_result1 = web_app.change_property_hardassert(property,value)
    assert (bln_result1, False)



@then('the user should not be able to connect to another device')
def the_user_should_not_be_able_to_connect_to_another_device():
    """the user should not be able to connect to another device."""
    print("Trying to connect 2 devices at once")
    bln_result = web_app.connect_to_device2()
    assert(bln_result, False)


@then('the user should not be able to get the state of the device')
def the_user_should_not_be_able_to_get_the_state_of_the_device():
    """the user should not be able to get the state of the device."""
    print("Trying to get status with device disconnected")
    bln_result1 = web_app.get_state()
    assert(bln_result1, False)
