from dnacentersdk import DNACenterAPI
from pprint import pprint
# from dnacreds import DNAC_USER, DNAC_PASS, DNAC_URL, DNAC_VER
import os
DNAC_USER = os.environ.get("DNA_CENTER_USERNAME")
DNAC_PASS = os.environ.get("DNA_CENTER_PASSWORD")
DNAC_URL = os.environ.get("DNA_CENTER_BASE_URL")
DNAC_VER = os.environ.get("DNA_CENTER_VERSION")

api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version=DNAC_VER, verify=False)

mydevice = api.devices.get_device_list(serialNumber='FJC25051UUC')

pprint(mydevice)
