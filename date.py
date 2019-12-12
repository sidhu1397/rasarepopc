# import datetime
#
# s= datetime.datetime.now()
# d =s.strftime("%Y-%m-%d")
# print(d)

from datetime import datetime
curr_time = datetime.now()
formatted_time = curr_time.strftime('%S')
print (type(formatted_time))

sec = int(formatted_time)
print(sec)
if(sec%10 == 0):
    print("every ten seconds")