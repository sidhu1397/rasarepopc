# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

#

# import sys
# sys.path.insert(0,'c:\\users\\admin\\anaconda3\\lib\\site-packages\\rasa\\core\\channels\\')
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa.core.channels.botframework import BotFrameworkInput
import pyodbc
import requests

# im going to perform a second commit
# seperately commiting only my master branch
import logging

import engineio
import six


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

class enterprojhandler(Action):
    def name(self):  # type: () -> Text
        return "action_enterproj"

    def run(
            self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain,  # type:  Dict[Text, Any]
    ):  # type: (...) -> List[Dict[Text, Any]]
        dispatcher.utter_message("Enterproj services are")
        dispatcher.utter_image_url("https://sidwebpage.s3.us-east-2.amazonaws.com/website/hanonlogo.png")
        conn = pyodbc.connect(Driver='{ODBC Driver 17 for SQL Server}', Server='localhost\SQLEXPRESS',
                              Database='testing',
                              Trusted_Connection='yes')

        cursor = conn.cursor()
        cursor.execute('select payload from sample where notification=\'yes\';')
        for row in cursor:
            print(row)
            requests.post("https://48527a34.ngrok.io/webhooks/botframework/webhook", data=row)


        payload = {}


        # payload["from"]=BotFrameworkInput.userdata["from"]
        # print(payload)

        # message = {
        #     "type": "video",
        #     "payload": {
        #         "src": "https://sidwebpage.s3.us-east-2.amazonaws.com/website/rasabot.mp4"
        #     }
        # }
        #
        # dispatcher.utter_attachment(message)

        # buttons = []
        # b1 = {"title": "enterproj", "payload": "/mood_unhappy"}
        # buttons.append(b1)
        # dispatcher.utter_button_message("mybutton", buttons)
        # s = {}
        # s["data"] = {
        #     "type": "AdaptiveCard",
        #     "version": "1.0",
        #     "body": [
        #         {
        #             "type": "TextBlock",
        #             "text": "Here is a ninja cat"
        #         },
        #         {
        #             "type": "Image",
        #             "url": "http://adaptivecards.io/content/cats/1.png"
        #         }
        #     ]
        # }
        # dispatcher.utter_custom_json(s)


class subscribeunix(Action):
    def name(self):  # type: () -> Text
        return "action_subscribe_unix_monitor"

    def run(
            self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain,  # type:  Dict[Text, Any]
    ):  # type: (...) -> List[Dict[Text, Any]]
        select_menu = {"type": "message", "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.hero",
                "content": {
                    "title": "unix machine monitoring",
                    "subtitle": "",
                    "text": "Do you want to subscribe to receive notifications pertaining to unix machine such as alerts?",
                    "buttons": [
                        {
                            "type": "imBack",
                            "title": "Yes",
                            "value": "yes i would like to recieve notification"
                        },
                        {
                            "type": "imBack",
                            "title": "No",
                            "value": "no i dont want notification"
                        },

                    ]
                }
            }
        ]}
        dispatcher.utter_custom_json(select_menu)
        # vid = {
        #     "type": "message", "attachments":
        #         [
        #             {
        #     'contentType': 'application/vnd.microsoft.card.adaptive',
        #     "content":   {
        #         "type": "AdaptiveCard",
        #         "body":     [
        #                 {
        #                 "type": "Media",
        #                 "poster": "https://adaptivecards.io/content/poster-video.png",
        #                 "sources":  [
        #                         {
        #                         "mimeType": "video/mp4",
        #                         "url": "https://adaptivecardsblob.blob.core.windows.net/assets/AdaptiveCardsOverviewVideo.mp4"
        #                         }   ]
        #
        #
        #
        #                     }
        #                         ]
        #                             }
        #                                     }
        #             ]
        # }
        # dispatcher.utter_custom_json(vid)
        #     dict =tracker.current_state()
        #     print(dict)
        #     vid_button ={
        #     "type": "message", "attachments":
        #         [
        #             {
        #     'contentType': 'application/vnd.microsoft.card.adaptive',
        #     "content":   {
        #                       "type": "AdaptiveCard",
        #                       "version": "1.0",
        #                       "body": [
        #                         {
        #                           "type": "TextBlock",
        #                           "text": "Hanon tutorial video"
        #                         }
        #                       ],
        #                       "actions": [
        #                         {
        #                           "type": "Action.OpenUrl",
        #                           "title": "Hanon FAQ Video",
        #                           "url": "https://rasabot.s3.us-east-2.amazonaws.com/Hanon.mp4"
        #                         }
        #                       ]
        #                 }
        #             }]}
        #
        #     dispatcher.utter_custom_json(vid_button)



class notifcationyes(Action):
    def name(self):  # type: () -> Text
        return "action_yes"

    def run(
            self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain,  # type:  Dict[Text, Any]
    ):  # type: (...) -> List[Dict[Text, Any]]
        # name = payload['from']['name']
        senderid = tracker.sender_id
        conn = pyodbc.connect(Driver='{ODBC Driver 17 for SQL Server}', Server='localhost\SQLEXPRESS',
                              Database='testing',
                              Trusted_Connection='yes')
        cursor = conn.cursor()
        query = "update sample set notification='yes' where id = \'{0}\'".format(senderid)
        print(query)
        cursor.execute(query)
        cursor.commit()
        dispatcher.utter_message("You are subscribed to receive notifications regarding unix machine")


class fileuploadhandler(Action):
    def name(self):  # type: () -> Text
        return "action_Filehandler"
    def run(
        self,
        dispatcher,  # type: CollectingDispatcher
        tracker,  # type: Tracker
        domain,  # type:  Dict[Text, Any]
    ):  # type: (...) -> List[Dict[Text, Any]]
        tfname=tracker.sender_id
        tfname=str(tfname)
        tfname=tfname.replace(":","")
        fname = "C:\\Users\Admin\\rasafilehandler\\" + tfname + ".txt"
        Myfile =open(fname,"r")
        contents = Myfile.read()
        Myfile.close()
        dispatcher.utter_message("your file url = {0}".format(contents))
        import os
        os.remove(fname)
        print("file removed")


