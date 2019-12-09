# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, json, request

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


@app.route('/about/<name>,<age>')
def display_arguements(name, age):
    s = 'Name = {0} and age = {1}'.format(name, age)
    return s


@app.route('/posthandler', methods=['POST'])
def display_post_request():
    print(request.get_json())
    res = request.get_json()
    return "post data Name ={0} and Org = {1}".format(res['name'], res['org'])


app.run()
