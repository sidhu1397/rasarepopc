from flask import Flask, send_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    fname = "C:\\Users\\Admin\\PycharmProjects\\rasabot1\\AddTeamMember2.jpg"
    return send_file(fname, mimetype='image/jpg')

if __name__ == '__main__':
    app.run()