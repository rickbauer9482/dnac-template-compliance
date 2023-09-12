from dnacentersdk import DNACenterAPI
from pprint import pprint
import os
import json

# Importing difflib
import difflib

DNAC_USER = os.environ.get("DNA_CENTER_USERNAME")
DNAC_PASS = os.environ.get("DNA_CENTER_PASSWORD")
DNAC_URL = os.environ.get("DNA_CENTER_BASE_URL")
DNAC_VER = os.environ.get("DNA_CENTER_VERSION")

api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version=DNAC_VER, verify=False)

dna_template = api.configuration_templates.get_template_details(template_id='a5b3ae34-a19f-42a1-b2f7-16b2900c763c', latest_version=None)

# pprint(mytemplate['templateContent'])
# pprint(mytemplate)

# write dna_template response to template-out.txt
with open('dna-template-out.txt', 'w') as dna-template-out:
    dna-template-out.write(json.dumps(dna-template['templateContent']))
    

# open master-template-out.txt from github
master-f = open('master-template.json', 'r')
data = json.load(master-f)
# print(data[0]['templateContent'])

with open('master-template.txt', 'w') as convert-master-f:
    convert-master-f.write(json.dumps(data[0]['templateContent']))
# close files
dna-template-out.close()
convert-master-f.close()

# Open File in Read Mode
file_1 = open('master-template.txt', 'r')
file_2 = open('dna-template-out.txt', 'r')
 
print("Comparing files ", " @ " + 'master-template.txt', " # " + 'dna-template-out.txt', sep='\n')
 
file_1_line = file_1.readline()
file_2_line = file_2.readline()
 
# Use as a Counter
line_no = 1
 
print()
 
with open('master-template.txt') as file1:
    with open('dna-template-out.txt') as file2:
        same = set(file1).intersection(file2)
 
print("Common Lines in Both Files")
 
for line in same:
    print(line, end='')
 
print('\n')
print("Difference Lines in Both Files")
while file_1_line != '' or file_2_line != '':
 
    # Removing whitespaces
    file_1_line = file_1_line.rstrip()
    file_2_line = file_2_line.rstrip()
 
    # Compare the lines from both file
    if file_1_line != file_2_line:
       
        # otherwise output the line on file1 and use @ sign
        if file_1_line == '':
            print("@", "Line-%d" % line_no, file_1_line)
        else:
            print("@-", "Line-%d" % line_no, file_1_line)
             
        # otherwise output the line on file2 and use # sign
        if file_2_line == '':
            print("#", "Line-%d" % line_no, file_2_line)
        else:
            print("#+", "Line-%d" % line_no, file_2_line)
 
        # Print a empty line
        print()
 
    # Read the next line from the file
    file_1_line = file_1.readline()
    file_2_line = file_2.readline()
 
    line_no += 1
 
file_1.close()
file_2.close()
