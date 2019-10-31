import pyodbc
import json

payload = {"text": "im not good",
           "textFormat": "plain",
           "type": "message",
           "id": "1572414086010",
           "channelId": "msteams",
           "serviceUrl": "https://smba.trafficmanager.net/in/",
           "from": {"id": "29:1mhe1WmNnSJ5Xn1CyJj3tOOpB4bP-YyyH2Qt8hBcg90Mxmsa_8gAxh56tN-mWhlq7IN1EeWBF8bT5-qXNO4fJig",
                    "name": "sidharth sridhar", "aadObjectId": "7bd287c0-5650-49de-ba51-028f4779e1e1"},
           "conversation": {"conversationType": "personal", "tenantId": "4dc0ce17-0629-4935-804f-c293477c4a19",
                            "id": "a:1dQmsB9fHNypyMu4yI5vIbIIs16rfuom8md3EgzpD4_7wGJTr1563XI0fJl04Od4VN88MxmvunePGKMbJbtO2TE92MmNipp6_KyQNXGXBaUzFZaTBZ8rY6Rz1uvD0OXTP"},
           "recipient": {"id": "28:686b1955-efff-4ea5-b2f2-d16ccc75b674", "name": "pythonbot"}
           }

#for double quotes
z = json.dumps(payload)
#print(z)

name = payload['from']['name']
conn = pyodbc.connect(Driver='{ODBC Driver 17 for SQL Server}', Server='localhost\SQLEXPRESS', Database='testing',
                      Trusted_Connection='yes')
cursor = conn.cursor()

c = """
create or alter procedure notify @name varchar(20),@payload nvarchar(4000),@id nvarchar(4000)
as
declare cname cursor for select name from testing.dbo.sample;
declare @checkname varchar(20)
declare @count int = 0;
open cname;
fetch next from cname into @checkname;
while @@FETCH_STATUS = 0
begin
if (@name = @checkname)
begin
   set @count = @count + 1
end
fetch next from cname into @checkname
end
if(@count=0)
begin
insert into sample values(@id,@name,@payload,'no')
end
"""

# cursor.execute("use testing;")
# cursor.execute("select * from testing.dbo.student;")
# for row in cursor:
#     print(row)
query = "exec notify @name='{0}',@payload = N'{1}',@id='{2}';".format(payload['from']['name'],z,payload["from"]["id"])

cursor.execute(c)
cursor.execute(query)
cursor.execute("insert into student values(4)")
cursor.execute("select * from sample")

for row in cursor:
    print(row)


cursor.commit()
print("prgram ended")
print(payload["from"]["id"])
