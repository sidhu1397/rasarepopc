import flask
from flask import request, jsonify
# import pythoncom
import json
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.assistant_v2 import MessageInput
import requests
import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

MICROSOFT_OAUTH2_URL = "https://login.microsoftonline.com"

MICROSOFT_OAUTH2_PATH = "botframework.com/oauth2/v2.0/token"


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hanon Project Webservice</h1>" \
           "<p>This site is a prototype API Hanon systems Proof of concept</p>"


MICROSOFT_OAUTH2_URL = "https://login.microsoftonline.com"

MICROSOFT_OAUTH2_PATH = "botframework.com/oauth2/v2.0/token"


@app.route('/teamsrequest', methods=['POST'])
def handlerequest():
    print(request.get_json())
    res = request.get_json()
    print(res['text'])
    message = get_result_watson(res)

    head = get_headers(res)
    for msg_type in message['output']['generic']:
        if msg_type['response_type'] == 'text':
            send_state = preapre_text(res, head, msg_type['text'])
        elif str(msg_type['response_type'] == 'image'):
            prepare_image(res, head, msg_type['source'])
        else:
            prepare_text(res,head,"Unknown message type {0}".format(msg_type['response_type']))    

    # prepare text message

    print(send_state)

    return "Received message"


def get_headers(res):
    token_expiration_date = datetime.datetime.now()
    # if token_expiration_date < datetime.datetime.now():
    uri = f"{MICROSOFT_OAUTH2_URL}/{MICROSOFT_OAUTH2_PATH}"
    grant_type = "client_credentials"
    scope = "https://api.botframework.com/.default"
    payload = {
        "client_id": "c8a478c5-ea2a-4d0f-8a51-64338a369f9e",
        "client_secret": "-sTTTc7721E-TEQEeDwNF-jsKXtkLQH-",
        "grant_type": grant_type,
        "scope": scope,
    }

    token_response = requests.post(uri, data=payload)
    print("token response{0}".format(token_response))
    if token_response.ok:
        token_data = token_response.json()
        access_token = token_data["access_token"]
        token_expiration = token_data["expires_in"]

        delta = datetime.timedelta(seconds=int(token_expiration))
        token_expiration_date = datetime.datetime.now() + delta

        headers = {
            "content-type": "application/json",
            "Authorization": "Bearer %s" % access_token,
        }
        return headers
    else:
        print("Could not get BotFramework token")
        return "Could not get BotFramework token"


def get_result_watson(res):
    authenticator = IAMAuthenticator('api key')
    assistant = AssistantV2(
        version='2018-09-20',
        authenticator=authenticator)
    assistant.set_service_url(
        'URL')

    #########################
    # Sessions
    #########################

    session = assistant.create_session("assisstant id").get_result()
    print(json.dumps(session, indent=2))

    # assistant.delete_session("e2963d8d-2057-4b4c-a90d-bf36309371f9", session).get_result()

    #########################
    # Message
    #########################

    message = assistant.message(
        "assisstant id",
        session['session_id'],
        input={'text': res['text']}
    ).get_result()
    print("watson response = {0}".format(json.dumps(message, indent=2)))
    return message


def preapre_text(res, head, msg_text):
    uri = f"{res['serviceUrl']}v3/"
    data = {
        "type": "message",
        "recipient": {"id": res['recipient']['id']},
        "from": res['from'],
        "channelData": {"notification": {"alert": "true"}},
        "text": msg_text,
    }
    post_message_uri = "{0}conversations/{1}/activities".format(
        uri, res['conversation']["id"]
    )
    response = requests.post(post_message_uri, headers=head, data=json.dumps(data))
    print(response)
    return response


def prepare_image(res, head, src):
    hero_content = {
        "contentType": "application/vnd.microsoft.card.hero",
        "content": {"images": [{"url": src}]},
    }

    image_message = {"attachments": [hero_content]}
    uri = f"{res['serviceUrl']}v3/"
    data = {
        "type": "message",
        "recipient": {"id": res['recipient']['id']},
        "from": res['from'],
        "channelData": {"notification": {"alert": "true"}},
        "text": "",
    }
    data.update(image_message)
    post_message_uri = "{0}conversations/{1}/activities".format(
        uri, res['conversation']["id"]
    )
    response = requests.post(post_message_uri, headers=head, data=json.dumps(data))
    print(response)
    return response


app.run()
