import pysnow
import socket

c = pysnow.Client(host='dev63230.service-now.com', user='admin', password='Agile@2020')
c.parameters.exclude_reference_link = True
new_record = {
    'short_description': 'Service now ticket for unix monitoring',
    'description': 'This is a Service now ticket for unix monitoring'
}
# Define a resource, here we'll use the incident table API
incident = c.resource(api_path='/table/incident')

try:

    response = incident.get(query={'state': 2,'sys_created_by': 'sidarth','assigned_to':'6816f79cc0a8016401c5a33be04be441','sys_created_on':'2019-12-06'})

except socket.gaierror as msg:
    print(msg)
# print(response.one())

# Iterate over the result and print out `sys_id` of the matching records.
# print(response.first())
for record in response.all():
    print(record)
# 'sys_created_by': 'sidarth'
# 'value':6816f79cc0a8016401c5a33be04be441
#2019-12-06 13:34:42
