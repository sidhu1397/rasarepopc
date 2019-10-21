# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#im going to perform a second commit
#seperately commiting only my master branch
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
        message = {
            "type": "video",
            "payload": {
                "src": "https://sidwebpage.s3.us-east-2.amazonaws.com/website/rasabot.mp4"
            }
        }

        dispatcher.utter_attachment(message)
        buttons = []
        b1 = {"title": "enterproj", "payload": "/mood_unhappy"}
        buttons.append(b1)
        dispatcher.utter_button_message("mybutton", buttons)
        s = {}
        s["data"] = {
            "type": "AdaptiveCard",
            "version": "1.0",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Here is a ninja cat"
                },
                {
                    "type": "Image",
                    "url": "http://adaptivecards.io/content/cats/1.png"
                }
            ]
        }
        dispatcher.utter_custom_json(s)
