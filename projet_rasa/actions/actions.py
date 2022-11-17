# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from db.database import Database


class ActionGiveSchedule(Action):

    def name(self) -> Text:
        return "action_give_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(tracker.get_slot("section"))
        print(tracker.get_slot("group"))
        result=list(filter(lambda item: self.get_schedule(item, (tracker.get_slot("section"),tracker.get_slot("group"))),Database().select()))
        print (result)
        dispatcher.utter_message(text=f'Today you have class at {result[0][4]}')

       

        return []
    def get_schedule(self,item,data):
        if(item[0]==data[0] and item[1]==data[1]):
            return True
        else: 
            return False