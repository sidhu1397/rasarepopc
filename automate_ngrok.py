# import os
# a = os.system('ngrok http 5005')
# print(a)


import subprocess
cmd = ['ngrok http 5005']
output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
print(output)
