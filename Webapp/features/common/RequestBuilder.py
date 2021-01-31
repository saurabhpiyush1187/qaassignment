import requests
import json
import yaml

from requests.auth import HTTPBasicAuth, HTTPDigestAuth, HTTPProxyAuth
from requests_ntlm import HttpNtlmAuth

class RequestBuilder:

    """
    Description:
        |  This class provides methods to build a URI using base_url, path params and query params.
        |  This class allows user to modify path params and query params existing in an URI
        |  This class also let's user call a web service request.

    """


    def call_request(self, pstr_method, pstr_url, pdict_headers, **kwargs):
        """
        Description:
            |  This method allows user to call a Get/Post/Put/Post/Patch/Delete request

        :param pstr_method: Type of request. Get or Post etc..
        :type pstr_method: String
        :param pstr_url: Request URL
        :type pstr_url: String
        :param pdict_headers: Headers to call a request
        :type pdict_headers: dictionary
        :param pstr_json: json string
        :type pstr_json: String
        :param pstr_payload: payload dictionary
        :type pstr_payload: dictionary
        :param pdict_cookies: cookie dictionary
        :type pdict_cookies: dictionary
        :param pbln_allow_redirects:
        :type pbln_allow_redirects: boolean
        :param pstr_files: file path
        :type pstr_files: String
        :param pbln_verify:
        :type pbln_verify: boolean
        :param pstr_auth_type:
        :type pstr_auth_type: String
        :param pstr_auth_username:
        :type pstr_auth_username: String
        :param pstr_auth_password:
        :type pstr_auth_password: String
        :param ptimeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type ptimeout: float or tuple

        :return: response - response generated on calling a request
        .. code-block:: python

            call_request(“Get”,”https://www.samplesite.com/param1/param2”,headers={“Accept”:”application/json”})
            call_request(“Post”,”https://www.samplesite.com/param1/param2”,headers={“Accept”:”application/json”},pstr_payload=’{“KOU”:”123456”}’, pbln_allow_redirects=True)

        .. note::
            |  pstr_method (String) :
            |  Accepts: Get, Post,Put, Patch or Delete
            |  Correct: get/GET/Get
            |  Wrong: gEt/GEt
            |
            |  pstr_auth_type(String) :
            |  Accepts: basic, ntlm, digest, proxy
            |
            |  Default Values for Kwargs:
            |  1. Default value of **kwargs parameter pstr_json is None
            |  2. Default value of **kwargs parameter pstr_payload is None
            |  3. Default value of **kwargs parameter pdict_cookies is empty dict({})
            |  4. Default value of **kwargs parameter pbln_allow_redirects is False
            |  5. Default value of **kwargs parameter pstr_files is None
            |  6. Default value of **kwargs parameter pbln_verify is False
            |  7. Default value of **kwargs parameter ptimeout is None

        """
        try:
            response=''
            if pstr_url == "":
                return None
            pstr_json = kwargs.get('pstr_json', None)
            pstr_payload = kwargs.get('pstr_payload', None)
            pdict_cookies = kwargs.get('pdict_cookies', {})
            pbln_allow_redirects = kwargs.get('pbln_allow_redirects', False)
            pstr_files = kwargs.get('pstr_files', None)
            pbln_verify = kwargs.get('pbln_verify', False)
            ptimeout = kwargs.get('ptimeout', None)
            pdict_proxies = kwargs.get('pdict_proxies', None)

            str_auth_string = ""

            if pstr_method.islower() or pstr_method.isupper() or pstr_method.istitle():

                if pstr_method.capitalize() == "Get":
                    response = requests.get(pstr_url,
                                            headers=pdict_headers,
                                            verify=pbln_verify,
                                            allow_redirects=pbln_allow_redirects,
                                            cookies=pdict_cookies,
                                            auth=str_auth_string,
                                            data=pstr_payload,
                                            json=pstr_json,
                                            timeout=ptimeout,proxies=pdict_proxies
                                            )
                elif pstr_method.capitalize() == "Post":
                    if pstr_payload is not None:
                        response = requests.post(pstr_url,
                                                 headers=pdict_headers,
                                                 data=pstr_payload,
                                                 json=pstr_json,
                                                 verify=pbln_verify,
                                                 allow_redirects=pbln_allow_redirects,
                                                 cookies=pdict_cookies,
                                                 files=pstr_files,
                                                 auth=str_auth_string,
                                                 timeout=ptimeout,proxies=pdict_proxies
                                                 )
                    else:
                        raise Exception("Error-->Payload is missing")
                elif pstr_method.capitalize() == "Put":
                    if pstr_payload is not None:
                        response = requests.put(pstr_url,
                                                headers=pdict_headers,
                                                data=pstr_payload,
                                                verify=pbln_verify,
                                                allow_redirects=pbln_allow_redirects,
                                                cookies=pdict_cookies,
                                                files=pstr_files,
                                                auth=str_auth_string,
                                                timeout=ptimeout,proxies=pdict_proxies
                                                )
                    else:
                        raise Exception("Error-->Payload is missing")
                elif pstr_method.capitalize() == "Patch":
                    if pstr_payload is not None:
                        response = requests.patch(pstr_url,
                                                  headers=pdict_headers,
                                                  data=pstr_payload,
                                                  verify=pbln_verify,
                                                  allow_redirects=pbln_allow_redirects,
                                                  cookies=pdict_cookies,
                                                  files=pstr_files,
                                                  auth=str_auth_string,
                                                  timeout=ptimeout,proxies=pdict_proxies
                                                  )
                    else:
                        raise Exception("Error-->Payload is missing")
                else:
                    if pstr_method.capitalize() == "Delete":
                        response = requests.delete(pstr_url,
                                                   headers=pdict_headers,
                                                   verify=pbln_verify,
                                                   allow_redirects=pbln_allow_redirects,
                                                   cookies=pdict_cookies,
                                                   auth=str_auth_string,
                                                   data=pstr_payload,
                                                   json=pstr_json,
                                                   timeout=ptimeout,proxies=pdict_proxies
                                                   )

                return response
            else:
                raise Exception('Error-->The parameter pstr_method can only be lowercase/uppercase/camelcase '
                                'i.e, get/GET/Get and not something like gEt/GEt etc')
        except Exception as e:
                print(e)


    def get_value_from_yaml(self, pstr_filepath, pstr_key):
        """
        Description:
            |  This method fetched the value of the specified key from a yaml (.yml) file

        :param pstr_filepath: Path of the yml file
        :type pstr_filepath: String
        :param pstr_key: key for which value needs to be fetched
        :type pstr_key: String

        :return: value for specified key
        """
        try:
            if pstr_key == "":
                return None
            with open(pstr_filepath, 'r') as file:
                yamlstream = yaml.load(file)
                if pstr_key in yamlstream:
                    return yamlstream[pstr_key]
                else:
                    raise Exception('Error-->Key:' + pstr_key + ' is not present in the yaml file ' + pstr_filepath)
        except FileNotFoundError:
            print("File not found")


    def get_value_from_json(self, pstr_filepath, pstr_key):
        """
        Description:
            |  This method fetched the value of the specified key from a JSON(.json) file

        :param pstr_filepath: Path of the json file
        :type pstr_filepath: String
        :param pstr_key: key for which value needs to be fetched
        :type pstr_key: String

        :return: value for specified key
        """
        try:
            if pstr_key == "":
                return None
            with open(pstr_filepath, 'r') as file:
                jsonstream = json.load(file)
                if pstr_key in jsonstream:
                    return jsonstream[pstr_key]
                else:
                    raise Exception('Error-->Key:' + pstr_key + ' is not present in the json file ' + pstr_filepath)
        except FileNotFoundError:
            print("File not found")

    def get_response_statuscode(self, pobj_response_obj):
        """
        Description:
            |  This method returns status code of the response that is passed

        :param pobj_response_obj: Response object whose status code is needed
        :type pobj_response_obj: Object

        :return: status code integer
        """
        try:
            if pobj_response_obj is None:
                return None
            else:
                return pobj_response_obj.status_code
        except Exception as e:
            print(e)





    def get_response_time(self, pobj_response_obj, pstr_format="%s.%S"):
        """
        Description:
            |  This method returns response time in 3 different formats based on pstr_format.
            |  When
            |  (1) pstr_format == "%s.%f" then response time will be in the form of seconds and microseconds
            |  (2) pstr_format == "%s.%S" then response time will be in the form of seconds and milliseconds
            |  (3) pstr_format == "%M.%s" then response time will be in the form of minutes and seconds

        :param pobj_response_obj:
        :type pobj_response_obj: Response Object
        :param pstr_format: Default value is "%s.%S"
        :type pstr_format: String

        :return: float
        """
        try:
            if pobj_response_obj is None:
                return None
            if pstr_format not in ['%s.%f', '%s.%S', '%M.%s']:
                print("Incorrect Format")
            flt_sec_micro = pobj_response_obj.elapsed.total_seconds()
            if pstr_format == "%s.%f":
                return flt_sec_micro
            int_micro = pobj_response_obj.elapsed.microseconds
            int_milli = int_micro / 1000
            flt_sec_milli = float(str(int(flt_sec_micro)) + '.' + str(int_milli).split('.')[0])
            if pstr_format == "%s.%S":
                return flt_sec_milli
            flt_minutes = round((flt_sec_milli / 60), 4) # limiting values after decimal to 4
            if pstr_format == "%M.%s":
                return flt_minutes
        except Exception as e:
            print(e)



    def post_file(self, pstr_method, pstr_url, pdict_headers, **kwargs):
        """
                Description:
                    |  This method allows user to call a /Post/Put/Post/Patch/ request
                    |  Please use the Method Call Request for all your API needs
                    |  This method does not have any in built validation checks, so user should use this method discretely
                    |  This method is primarly created for posting files to API services directly with out any body

                :param pstr_method: Type of request. Post etc..
                :type pstr_method: String
                :param pstr_url: Request URL
                :type pstr_url: String
                :param pdict_headers: Headers to call a request
                :type pdict_headers: dictionary
                :param pstr_json: json string
                :type pstr_json: String
                :param pstr_payload: payload dictionary
                :type pstr_payload: dictionary
                :param pdict_cookies: cookie dictionary
                :type pdict_cookies: dictionary
                :param pbln_allow_redirects:
                :type pbln_allow_redirects: boolean
                :param pstr_files: file path
                :type pstr_files: String
                :param pbln_verify:
                :type pbln_verify: boolean
                :param pstr_auth_type:
                :type pstr_auth_type: String
                :param pstr_auth_username:
                :type pstr_auth_username: String
                :param pstr_auth_password:
                :type pstr_auth_password: String
                :param ptimeout: (optional) How long to wait for the server to send
                    data before giving up, as a float, or a :ref:`(connect timeout,
                    read timeout) <timeouts>` tuple.
                :type ptimeout: float or tuple

                :return: response - response generated on calling a request
                .. code-block:: python
                    file_content = open(File_Path, 'rb')
                    _files = {"KeyName": (file_name, file_content, file_type)}
                    post_file(“Post”,”https://www.samplesite.com/param1/param2”,headers={“Accept”:”application/json”},pstr_files=_files, pbln_allow_redirects=True) # we do not need payload for this post call

                .. note::
                    |  pstr_method (String) :
                    |  Accepts: Post,Put, Patch or Delete
                    |  Correct: Post/POST/Post
                    |  Wrong: pOSt
                    |
                    |  pstr_auth_type(String) :
                    |  Accepts: basic, ntlm, digest, proxy
                    |
                    |  Default Values for Kwargs:
                    |  1. Default value of **kwargs parameter pstr_json is None
                    |  2. Default value of **kwargs parameter pstr_payload is None
                    |  3. Default value of **kwargs parameter pdict_cookies is empty dict({})
                    |  4. Default value of **kwargs parameter pbln_allow_redirects is False
                    |  5. Default value of **kwargs parameter pstr_files is None
                    |  6. Default value of **kwargs parameter pbln_verify is False
                    |  7. Default value of **kwargs parameter ptimeout is None

                """
        try:
            response=''
            if pstr_url == "":
                return None
            pstr_json = kwargs.get('pstr_json', None)
            pstr_payload = kwargs.get('pstr_payload', None)
            pdict_cookies = kwargs.get('pdict_cookies', {})
            pbln_allow_redirects = kwargs.get('pbln_allow_redirects', False)
            pstr_files = kwargs.get('pstr_files', None)
            pbln_verify = kwargs.get('pbln_verify', False)
            pstr_auth_type = kwargs.get('pstr_auth_type', None)
            pstr_auth_username = kwargs.get('pstr_auth_username', None)
            pstr_auth_password = kwargs.get('pstr_auth_password', None)
            ptimeout = kwargs.get('ptimeout', None)

            str_auth_string = ""
            if not pstr_auth_type is None:
                pstr_auth_type = pstr_auth_type.lower()
                if pstr_auth_type == "basic":
                    str_auth_string = HTTPBasicAuth(pstr_auth_username, pstr_auth_password)
                elif pstr_auth_type == "ntlm":
                    str_auth_string = HttpNtlmAuth(pstr_auth_username, pstr_auth_password)
                elif pstr_auth_type == "proxy":
                    str_auth_string = HTTPProxyAuth(pstr_auth_username, pstr_auth_password)
                elif pstr_auth_type == "digest":
                    str_auth_string = HTTPDigestAuth(pstr_auth_username, pstr_auth_password)

            if pstr_method.islower() or pstr_method.isupper() or pstr_method.istitle():
                if pstr_method.capitalize() == "Post":
                    response = requests.post(pstr_url,
                                             headers=pdict_headers,
                                             data=pstr_payload,
                                             json=pstr_json,
                                             verify=pbln_verify,
                                             allow_redirects=pbln_allow_redirects,
                                             cookies=pdict_cookies,
                                             files=pstr_files,
                                             auth=str_auth_string,
                                             timeout=ptimeout
                                             )
                elif pstr_method.capitalize() == "Put":
                    response = requests.put(pstr_url,
                                            headers=pdict_headers,
                                            data=pstr_payload,
                                            verify=pbln_verify,
                                            allow_redirects=pbln_allow_redirects,
                                            cookies=pdict_cookies,
                                            files=pstr_files,
                                            auth=str_auth_string,
                                            timeout=ptimeout
                                            )
                elif pstr_method.capitalize() == "Patch":
                    response = requests.patch(pstr_url,
                                              headers=pdict_headers,
                                              data=pstr_payload,
                                              verify=pbln_verify,
                                              allow_redirects=pbln_allow_redirects,
                                              cookies=pdict_cookies,
                                              files=pstr_files,
                                              auth=str_auth_string,
                                              timeout=ptimeout
                                              )
                else:
                    if pstr_url == "":
                        return None
                return response
            else:
                raise Exception('Error-->The parameter pstr_method can only be lowercase/uppercase/camelcase '
                                'i.e, post/POST and not something like pOSt etc')
        except Exception as e:
            print(e)
