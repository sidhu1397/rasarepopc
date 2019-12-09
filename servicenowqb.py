import pysnow
# import datetime
#
# start = datetime(1970, 1, 1)
# end = datetime.now() - datetime.timedelta(days=20)
import datetime

s= datetime.datetime.now()
d =s.strftime("%Y-%m-%d")
print(d)

# Query incident records with number starting with 'INC0123', created between 1970-01-01 and 20 days back in time
qb = (
    pysnow.QueryBuilder()
    .field('state').equals('2')
    .AND()
    .field('assigned_to').equals('6816f79cc0a8016401c5a33be04be441')
    .AND()
    .field('sys_created_by').equals('sidarth')
    .AND()
    .field("sys_created_on").starts_with(str(d))
)

c = pysnow.Client(host='dev63230.service-now.com', user='admin', password='Agile@2020')
c.parameters.exclude_reference_link = True
# new_record = {
#     'short_description': 'Service now ticket for unix monitoring',
#     'description': 'This is a Service now ticket for unix monitoring'
# }
# # Define a resource, here we'll use the incident table API
incident = c.resource(api_path='/table/incident')

iterable_content = incident.get(query=qb)

for record in iterable_content.all():
    print(record)
print(type(iterable_content))
# print(iterable_content)
