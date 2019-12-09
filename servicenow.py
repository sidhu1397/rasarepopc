# global incident
# global incidentnumber
import socket
import pysnow
import json
#
# # Set the payload
#
c = pysnow.Client(host='dev63230.service-now.com', user='admin', password='Agile@2020')
new_record = {
    'short_description': 'Service now ticket for unix monitoring',
    'description': 'This is a Service now ticket for unix monitoring'
}
# Define a resource, here we'll use the incident table API
incident = c.resource(api_path='/table/incident')
result = incident.create(payload=new_record)
print(result)
# incident.
print(result)
res2 = result._response._content
print(res2)
print("res2val = {0}".format(res2))
res3 = res2.decode('utf-8')
res3 = json.loads(res3)
print(res3)
print("hi")
print(res3['result']['number'])
incidentnumber = res3['result']['number']
print(incidentnumber)
#
#

update = {'state': 2, 'caller_id': 'System Administrator'}
updated_record = incident.update(query={'number': incidentnumber}, payload=update)
# update = {'state': 7, 'caller_id': 'System Administrator',
#           "close_code": "Closed/Resolved By Caller", "close_notes": "Closed by API"}
# updated_record = incident.update(query={'number': incidentnumber}, payload=update)
#
# print(" service now incident is closed")

# import socket
# import pysnow
#



# try:
#
#     response = incident.get(query={'state':1},stream = True)
#
# except socket.gaierror as msg:
#     print(msg)
# print(response.first())

# Iterate over the result and print out `sys_id` of the matching records.
# for record in response.all():
#     print(record['number'])

