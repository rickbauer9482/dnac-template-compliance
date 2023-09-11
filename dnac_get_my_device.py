from dnacentersdk import DNACenterAPI
from pprint import pprint
# import os

# DNAC_USER = os.environ.get("DNA_CENTER_USERNAME")
# DNAC_PASS = os.environ.get("DNA_CENTER_PASSWORD")
# DNAC_URL = os.environ.get("DNA_CENTER_BASE_URL")
# DNAC_VER = os.environ.get("DNA_CENTER_VERSION")

api = DNACenterAPI(username=DNA_CENTER_USERNAME, password=DNA_CENTER_PASSWORD, base_url=DNA_CENTER_BASE_URL, version=DNA_CENETER_VERSION, verify=False)

mydevice = api.devices.get_device_list(serialNumber='FJC25051UUC')

pprint(mydevice)
