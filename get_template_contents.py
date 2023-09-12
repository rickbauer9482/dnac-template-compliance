from dnacentersdk import DNACenterAPI
from pprint import pprint
import os

DNAC_USER = os.environ.get("DNA_CENTER_USERNAME")
DNAC_PASS = os.environ.get("DNA_CENTER_PASSWORD")
DNAC_URL = os.environ.get("DNA_CENTER_BASE_URL")
DNAC_VER = os.environ.get("DNA_CENTER_VERSION")

api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version=DNAC_VER, verify=False)

mytemplate = api.configuration_templates.get_template_details(template_id='a5b3ae34-a19f-42a1-b2f7-16b2900c763c', latest_version=None)

pprint(mytemplate['templateContent'])
