import os
import json
from features.common.config_utils import ConfigUtils
from features.common.RequestBuilder import RequestBuilder
from features.common.common_utils import MICommonUtils



class WebApp:
    config_utils = ConfigUtils(os.getcwd())
    request_builder = RequestBuilder()
    mi_common_utils = MICommonUtils()

    def __init__(self):
        self.str_export_type = ""
        self.response = ""
        self.response_content= ""
        self.str_request_url = ""
        self.dict_success = {"success": True}
        self.dict_fail = {"success": False}

        self.state_keys =['name','ip','color','brightness']


    def validate_reponse(self):
        """
        Description:
        	|  This method calls the is_responsevalid from comon_utils to validate the response code
        :return: None
        """
        try:
            bln_response = self.mi_common_utils.is_responsevalid(self.response)
            return bln_response
        except Exception as e:
            print("Error in validation response-->" + str(e))



    def list_devices(self):
        try:
            dict_service_disc = self.config_utils.get_servicedescription(
                "web_app" + os.sep + "web_app_description.yml", "list_devices")
            str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] + dict_service_disc[
                "queryparams"]
            headers = dict_service_disc["headers"]
            self.response = self.request_builder.call_request(dict_service_disc["method"], str_request_url, headers)
            self.response_content = self.response.content
            assert self.mi_common_utils.is_reponsegenerated(self.response)
        except Exception as e:
            print(e)

    def validate_list_devices(self):
        try:
            bln_return = False
            response_json = json.loads(self.response_content)
            print(response_json)
            for i in range(len(response_json)):
                for key,value in response_json[i].items():
                    if key=='name' or key=='ip':
                        bln_return = True
            return bln_return

        except Exception as e:
            print(e)

    def disconnect_from_device(self):
        try:
            bln_root=False
            dict_service_disc = self.config_utils.get_servicedescription(
                "web_app" + os.sep + "web_app_description.yml", "disconnect_device")
            str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] + dict_service_disc[
                "queryparams"]
            headers = dict_service_disc["headers"]
            self.response = self.request_builder.post_file(dict_service_disc["method"], str_request_url, headers)
            self.response_content = self.response.content
            bln_response1= self.mi_common_utils.is_reponsegenerated(self.response)
            bln_validate_response= self.validate_reponse()
            response_json = json.loads(self.response_content)
            if bln_response1 == True and bln_validate_response == True and response_json == self.dict_success:
                print("Disconnected successully from devices")
                bln_root = True
            else:
                print("Unable to disconnect from device")
            return bln_root
        except Exception as e:
            print(e)

    def connect_to_device1(self):
        try:
            bln_root=False
            dict_service_disc = self.config_utils.get_servicedescription(
                "web_app" + os.sep + "web_app_description.yml", "connect_device1")
            str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] + dict_service_disc[
                "queryparams"]
            headers=dict_service_disc["headers"]
            payload = dict_service_disc["payload"]
            self.response = self.request_builder.post_file(dict_service_disc["method"], str_request_url,
                                                              headers, pstr_payload=payload)
            self.response_content = self.response.content
            bln_response1= self.mi_common_utils.is_reponsegenerated(self.response)
            bln_validate_response= self.validate_reponse()
            response_json = json.loads(self.response_content)
            if bln_response1==True and bln_validate_response == True and response_json == self.dict_success:
                print("Successfully connected to device1" + str(payload))
                bln_root = True
            else:
                print("Unable to connect to device1" + str(payload))
            return bln_root
        except Exception as e:
            print(e)

    def connect_to_device2(self):
        try:
            bln_root = False
            dict_service_disc = self.config_utils.get_servicedescription(
                "web_app" + os.sep + "web_app_description.yml", "connect_device2")
            str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] + dict_service_disc[
                "queryparams"]
            headers = dict_service_disc["headers"]
            payload = dict_service_disc["payload"]
            self.response = self.request_builder.post_file(dict_service_disc["method"], str_request_url,
                                                           headers, pstr_payload=payload)
            self.response_content = self.response.content
            bln_response1 = self.mi_common_utils.is_reponsegenerated(self.response)
            bln_validate_response = self.validate_reponse()
            response_json = json.loads(self.response_content)
            if bln_response1 == True and bln_validate_response == True and response_json == self.dict_success:
                bln_root = True
                print("Successfully connected to device2" + str(payload))
            else:
                print("Unable to connect to device2"+ str(payload))
            return bln_root
        except Exception as e:
            print(e)

    def get_state(self):
        try:
            self.state = {}
            bln_root = False
            bln_state= False
            dict_service_disc = self.config_utils.get_servicedescription(
                "web_app" + os.sep + "web_app_description.yml", "check_state")
            str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] + dict_service_disc[
                "queryparams"]
            headers = dict_service_disc["headers"]
            self.response = self.request_builder.call_request(dict_service_disc["method"], str_request_url, headers)
            self.response_content = self.response.content
            bln_response1 = self.mi_common_utils.is_reponsegenerated(self.response)
            bln_validate_response = self.validate_reponse()
            response_json = json.loads(self.response_content)
            for i in range(len(self.state_keys)):
                if self.state_keys[i] in response_json:
                    print("Getting device state..matching keys")
                    print(str(self.state_keys[i]) + " matched")
                    bln_state = True
                else:
                    print("Unknown keys in the state")
                    print(response_json)
                    bln_state = False
            if bln_state:
                self.state = dict(response_json)
            if bln_response1 == True and bln_validate_response == True and bln_state==True:
                print("State verified successfully of the device " + response_json["ip"])
                bln_root = True
            elif response_json == self.dict_fail:
                print("Unable to get state of the device..Device may be disconnected")
            else:
                print("Unable to get state of the device " + response_json["ip"])
            return bln_root
        except Exception as e:
            print(e)

    def change_property_hardassert(self,sub_property,value):
        try:
            self.return_response_json = {}
            bln_root = False
            dict_service_disc = self.config_utils.get_servicedescription(
                "web_app" + os.sep + "web_app_description.yml", "property_change")

            str_request_url = dict_service_disc["target_url"] + "/"+sub_property + dict_service_disc[
                "queryparams"]
            headers = dict_service_disc["headers"]
            payload = "{"+"\""+sub_property+"\""+":"+"\""+value+"\""+"}"
            self.response = self.request_builder.post_file(dict_service_disc["method"], str_request_url,
                                                           headers, pstr_payload=payload)
            self.response_content = self.response.content
            bln_response1 = self.mi_common_utils.is_reponsegenerated(self.response)
            bln_validate_response = self.validate_reponse()
            if bln_validate_response:
                response_json = json.loads(self.response_content)
                self.return_response_json = response_json
                if bln_response1 == True and response_json == self.dict_success:
                    print("Successfully changed the "+ sub_property+ " of device1" + str(payload))
                    bln_root = True
                elif response_json == self.dict_fail:
                    print("Unable to change" + sub_property + " of the device..Device may be disconnected or incorrect value")
                    print("Return Message is " + str(response_json))
                else:
                    print("Unable to connect to device1" + str(payload))
            return bln_root

        except Exception as e:
            print(e)

    def change_property_softassert(self,sub_property,value):
        try:
            self.return_response_json = {}
            dict_service_disc = self.config_utils.get_servicedescription(
                "web_app" + os.sep + "web_app_description.yml", "property_change")

            str_request_url = dict_service_disc["target_url"] + "/"+sub_property + dict_service_disc[
                "queryparams"]
            headers = dict_service_disc["headers"]
            payload = "{"+"\""+sub_property+"\""+":"+"\""+value+"\""+"}"
            self.response = self.request_builder.post_file(dict_service_disc["method"], str_request_url,
                                                           headers, pstr_payload=payload)
            self.response_content = self.response.content
            bln_response1 = self.mi_common_utils.is_reponsegenerated(self.response)
            bln_validate_response = self.validate_reponse()
            if bln_validate_response:
                response_json = json.loads(self.response_content)
                self.return_response_json = response_json
                if bln_response1 == True and response_json == self.dict_success:
                    print("Successfully changed the "+ sub_property+ " of device1" + str(payload))
                elif response_json == self.dict_fail:
                    print("Unable to change" + sub_property +" of the device..Device may be disconnected or incorrect value")
                    print("Return Message is "+ str(response_json))
                else:
                    print("Unable to connect to device1" + str(payload))
            else:
                self.return_response_json = self.request_builder.get_response_statuscode(self.response)
        except Exception as e:
            print(e)


    def check_response(self,result):
        try:
            if str(self.return_response_json).replace('\'',"\"") == result:
                print("Response successfully matched with " + str(result))
                return True
            else:
                print("Response code" + str(self.return_response_json))
                return False

        except Exception as e:
            print(e)


    def check_value_in_state(self,sub_property,value):
        try:
            if sub_property == "brightness":
                value= float(int(value))
            if self.state[sub_property]==value:
                print(str(value) +" successfully verified in the state")
                return True
            else:
                print(str(value) +" not successfully verified in the state")
                return False

        except Exception as e:
            print(e)

    def check_value_after_reconnect(self):
        try:
            pstr_old_state= self.state
            assert self.get_state()
            pstr_new_state = self.state

            bln_root =all(pstr_new_state[k] == v for k, v in pstr_old_state.items() if k in pstr_new_state)
            print("Expected result--->"+ str(pstr_old_state))
            print("Actual result--->" + str(pstr_new_state))

            return bln_root

        except Exception as e:
            print(e)


