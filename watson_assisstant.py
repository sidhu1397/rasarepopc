import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.assistant_v2 import MessageInput


a = MessageInput(text='How to activate a project in enterproj')

authenticator = IAMAuthenticator('9fkfyVgUNr_BeBQv7RYB_wGQhtOceof-wv5PeEzZgKzg')
assistant = AssistantV2(
    version='2018-09-20',
    authenticator=authenticator)
assistant.set_service_url('https://api.au-syd.assistant.watson.cloud.ibm.com/instances/698fa26f-1cb9-49dc-83c2-94b66c483130')

#########################
# Sessions
#########################

session = assistant.create_session("e2963d8d-2057-4b4c-a90d-bf36309371f9").get_result()
print(json.dumps(session, indent=2))

# assistant.delete_session("e2963d8d-2057-4b4c-a90d-bf36309371f9", session).get_result()

#########################
# Message
#########################


message = assistant.message(
    "e2963d8d-2057-4b4c-a90d-bf36309371f9",
    session['session_id'],
    input={'text':'how to activate a project in enterproj'}
 ).get_result()
print(json.dumps(message, indent=2))