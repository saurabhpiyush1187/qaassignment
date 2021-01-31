import yaml
from functools import reduce
import operator
import time
import os

class ConfigUtils(object):
    """
    Description:
        |  1. This class contains methods related to fetching data from config.yml and team_or_functionality_config.yml
        |  2. This class also contains methods to fetch base URLs, default user details, service descriptions and db configurations

    .. note::
        |  Create an object for this class as obj = ConfigUtils(os.getcwd(), 'team_config_filename')

    """

    def __init__(self, pstr_current_path, pstr_team_config_filename=None):
        """
        Description:
            |  This method is acts as a constructor

        :param pstr_current_path: pass this as os.getcwd()
        :type pstr_current_path: String
        :param pstr_team_config_filename:
        :type pstr_team_config_filename: String

        :return: None
        """
        self.current_path = pstr_current_path
        self.features_dir_path = self.get_features_dirpath()
        self.base_config = self.read_base_config_file()

        self.team_config = {}
        if pstr_team_config_filename is not None:
            self.team_config = self.read_team_config_file(pstr_team_config_filename)

    def get_config_filepath(self):
        """
        Description:
            |  This method fetches path of config.yml

        :return: String
        """
        try:
            str_filepath = self.get_project_path() + os.path.sep + "config.yml"
            return str_filepath
        except Exception as e:
            print("Error in get_config_filepath method-->" + str(e))

    def read_base_config_file(self):
        """
        Description:
            |  This method reads base config.yml file and loads the content into a dictionary object.

        :return: Dictionary
        """
        try:
            count = 0
            config = None
            while config is None and count < 30:
                try:
                    with open(self.get_config_filepath(), 'r') as config_yml:
                        config = yaml.load(config_yml)
                except Exception as e:
                    pass
                count = count + 1
                time.sleep(1)
            if config is None:
                raise Exception("Error Occurred while reading a config file")
            return config
        except Exception as e:
            print("Error in read_base_config_file method-->" + str(e))
            return None

    def read_team_config_file(self, pstr_filename):
        """
        Description:
            |  This method reads team_config.yml file and loads the content into a dictionary object.

        :return: Dictionary
        """
        try:
            if (str(pstr_filename).endswith(".yml")):
                with open(self.get_configuration_dirpath() + os.sep + pstr_filename, 'r') as config_yml:
                    config = yaml.load(config_yml)
                return config
            else:
                raise Exception("Given file is not in yaml format")
        except Exception as e:
            print("Error in read_team_config_file method-->" + str(e))

    def get_project_path(self):
        """
        Description:
            |  This method fetches path of the root Project folder

        :return: String
        """
        try:
            return os.path.dirname(self.features_dir_path)
        except Exception as e:
            print("Error in get_project_path method-->" + str(e))

    def get_features_dirpath(self):
        """
        Description:
            |  This method fetches path of the features directory

        :return: String
        """
        try:
            str_currentdir_path = self.current_path
            str_currentdir_name = os.path.basename(str_currentdir_path)
            while not str_currentdir_name == "features":
                if os.sep + "features" in str_currentdir_path:
                    str_currentdir_path = os.path.dirname(os.path.abspath(str_currentdir_path))
                    str_currentdir_name = os.path.basename(str_currentdir_path)

                else:
                    str_currentdir_path = os.path.abspath(str_currentdir_path) + os.sep + "features"
                    str_currentdir_name = os.path.basename(str_currentdir_path)

            return str_currentdir_path
        except Exception as e:
            print("Error in get_features_dirpath method-->" + str(e))


    def get_configuration_dirpath(self):
        """
        Description:
            |  This method fetches path of the features/configuration directory

        :return: String
        """
        try:
            return os.path.join(self.features_dir_path, "configuration")
        except Exception as e:
            print("Error in get_configuration_dirpath method-->" + str(e))

    def get_valuefromyaml_keypath(self, pstr_yaml_filepath, pstr_keypath, pstr_delimiter='/'):
        """
        Description:
            |  This method fetches value of a key from a yaml file

        :param pstr_yaml_filepath:
        :type pstr_yaml_filepath: String
        :param pstr_keypath:
        :type pstr_keypath: String

        :return: List
        Examples:
            |  An example of pstr_keypath is root/level1/level2/key

        """
        try:
            with open(pstr_yaml_filepath, 'r') as config_yml:
                config = yaml.load(config_yml)
            lst_key = pstr_keypath.split(pstr_delimiter)
            return reduce(operator.getitem, lst_key, config)
        except Exception as e:
            print('Error in get_valuefromyaml_keypath method -->' + str(e))

    def get_valuefrom_configobject(self, pobj_config, pstr_keypath, pstr_delimiter='/'):
        """
        Description:
            |  This method fetches value of a key from a yaml file

        :param pobj_config:
        :type pobj_config: Dictionary
        :param pstr_keypath:
        :type pstr_keypath: String

        :return: List
        Examples:
            |  An example of pstr_keypath is root/level1/level2/key

        """
        try:
            lst_key = pstr_keypath.split(pstr_delimiter)
            return reduce(operator.getitem, lst_key, pobj_config)
        except Exception as e:
            print('Error in get_valuefrom_configobject method-->' + str(e))


    def fetch_base_url(self):
        """
        Description:
            |  This method fetches base_url for the environment selected based on the values applied for the keys execution_environment and environment_type in the config.yml

        :return: String
        """
        try:
            str_execution_environment = self.fetch_execution_environment()
            str_environment_type = self.fetch_environment_type()
            str_base_url = self.base_config["env"][str_execution_environment][str_environment_type]["base_url"]
            return str_base_url
        except Exception as e:
            print("Error in fetch_base_url method-->" + str(e))

    def fetch_environment_type(self):
        """
        Description:
            |  This method fetches the environment type from config.yml

        :return: String
        """
        try:
            return self.base_config.get("environment_type")
        except Exception as e:
            print("Error in fetch_environment_type method-->" + str(e))

    def fetch_execution_environment(self):
        """
        Description:
            |  This method fetches the execution environment from config.yml

        :return: String
        """
        try:
            return self.base_config.get("execution_environment")
        except Exception as e:
            print("Error in fetch_execution_environment method-->" + str(e))



    def fetch_servicedescription_path(self):
        """
        Description:
            |  This method fetches path of the features/services/service_description directory

        :return: String
        """
        try:
            str_service_description_path = self.base_config["service_description"]
            str_service_description_path = os.path.join(self.features_dir_path, str_service_description_path)
            return str_service_description_path
        except Exception as e:
            print("Error in fetch_servicedescription_path method-->" + str(e))

    def fetch_servicepayload_path(self):
        """
        Description:
            |  This method fetches path of the features/services/payloads directory

        :return: String
        """
        try:
            str_service_payloads_path = self.base_config["service_payloads"]
            str_service_payloads_path = os.path.join(self.features_dir_path, str_service_payloads_path)
            return str_service_payloads_path
        except Exception as e:
            print("Error in fetch_servicepayload_path method-->" + str(e))



    def fetch_target_url(self, pstr_target_key):
        """
        Description:
            |  This method returns the target_url mentioned in the team_config.yml based on the target_url key mentioned.

        :param pstr_target_key:
        :type pstr_target_key: String

        :return: String
        """
        try:
            str_execution_environment = self.fetch_execution_environment()
            str_environment_type = self.fetch_environment_type()
            str_target_url = self.team_config["env"][str_execution_environment][str_environment_type][pstr_target_key]
            return str_target_url
        except Exception as e:
            print("Error in fetch_target_url method-->" + str(e))

    def get_servicedescription(self, pstr_service_desc_relfilepath, pstr_keypath):
        """
        Description:
            |  This method fetches entire service description of a particular service mentioned in service description yaml file.
            |  The service description yaml file contains below keys
            |  method:
            |  endpoint:
            |  queryparams:
            |  headers:
            |  payload:
            |  target_url:

        :param pstr_service_desc_relfilepath: Relative path of the service description file
        :type pstr_service_desc_relfilepath: String
        :param pstr_keypath:
        :type pstr_keypath: String

        :return: Dictionary
        .. code-block:: python

            Sample service description appears as

            entity_search:
                method: GET
                endpoint: "/.Services.Search.Service/v2/typeahead/query"
                queryparams: "?start=0&rows=15&SearchToken=Down2Earth II&Catalogs=funds&RequestType=2"
                headers: {'Authorization': 'Bearer', 'Content-Type':'application/json'}
                payload: None
                target_url: target_url_1

        """
        try:
            dict_service_desc = {}
            str_service_desc_path = os.path.join(self.fetch_servicedescription_path(), pstr_service_desc_relfilepath)
            dict_service_description = self.get_valuefromyaml_keypath(str_service_desc_path, pstr_keypath)

            dict_service_desc["target_url"] = self.fetch_base_url()


            dict_service_desc["method"] = dict_service_description.get("method")
            dict_service_desc["endpoint"] = dict_service_description.get("endpoint")
            if dict_service_description.get("queryparams") == "None":
                dict_service_desc["queryparams"] = ""
            else:
                dict_service_desc["queryparams"] = dict_service_description.get("queryparams")
            if dict_service_description.get("headers") == "None":
                dict_service_desc["headers"] = {}
            else:
                dict_service_desc["headers"] = dict_service_description.get("headers")
            dict_service_desc["payload"] = dict_service_description.get("payload", "None")
            if not dict_service_desc["payload"] == "None":
                str_payload_path = os.path.join(self.fetch_servicepayload_path(), dict_service_desc["payload"])
                with open(str_payload_path, 'r') as file:
                    str_file_data = file.read()
                    dict_service_desc["payload"] = str_file_data
            return dict_service_desc
        except Exception as e:
            print("Error in get_servicedescription method-->" + str(e))



