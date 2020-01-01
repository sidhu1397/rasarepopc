# fname = ['f1.txt','f2.txt','f3.txt','f4.txt','f5.txt','f6.txt','f7.txt','f8.txt','f9.txt','f10.txt','f11.txt','f12.txt',]
# count =0
# for x in range(12):
#    f = open(fname[x],"w")
#    f.write("line 1")
#    f.close()
#     # print(fname[x])

f = open("server_info.txt","r")
content = f.readlines()
print(type(content))
print(content)
templist = []
for i in range(len(content)):

   templist = content[i].split(",")
   print("IP = {0} ,Username = {1} ,Password = {2}".format(templist[0],templist[1],templist[2]))

print(templist)