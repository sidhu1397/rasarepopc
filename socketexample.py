from aiohttp import web
import socketio

count = 0
# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App
# instance
sio.attach(app)

# we can define aiohttp endpoints just as we normally
# would with no change
async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

# If we wanted to create a new websocket endpoint,
# use this decorator, passing in the name of the
# event we wish to listen out for
@sio.on('message')
async def print_message(sid, message):
    # When we receive a new event of type
    # 'message' through a socket.io connection
    # we print the socket ID and the message
    global count
    from datetime import datetime
    import random
    curr_time = datetime.now()
    formatted_time = curr_time.strftime('%S')
    print("Socket ID: ", sid)
    print(type(formatted_time))

    sec = int(formatted_time)
    msg = str(message)
    print(sec)
    if sec in [40,41,42,43,44,45]:
        yaxis = random.randint(90, 93)
        await sio.emit('message', yaxis)
    else:
        yaxis = random.randint(30, 40)
        await sio.emit('message', yaxis)


    # if sec % 40 == 0 or msg == "critical":
    #     yaxis = random.randint(90,95)
    #     count = count + 1
    #     await sio.emit('message', yaxis)
    #
    # elif count == 5:
    #     count = 1
    #     yaxis = random.randint(50, 70)
    #     await sio.emit('message', yaxis)
    # else:
    #     yaxis = random.randint(50, 70)
    #     await sio.emit('message', yaxis)





# We bind our aiohttp endpoint to our app
# router
app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app)