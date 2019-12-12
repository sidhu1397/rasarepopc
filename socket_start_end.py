

from datetime import datetime

import socketio

sio = socketio.Client()
sio.connect('http://localhost:8080')
global count
count = 0
print("client connected")



while (True):

    f = open("C:\\Users\\Admin\\PycharmProjects\\rasabot1\\Start_end_time.txt","r")
    content = f.read()
    if str(content) == "starttime" and count == 0:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current start Time =", current_time)
        start_time = {"starttime": current_time}
        sio.emit('message', start_time)
        count = 1
        # sio.emit('end', "close")
        # del sio
    if str(content) == "endtime" and count == 1:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        end_time = {"endtime": current_time}
        print("Current end Time =", current_time)
        sio.emit('message', end_time)
        count = 0
    f.close()


