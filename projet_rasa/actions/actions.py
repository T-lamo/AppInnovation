# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# from db.database import Database
# from db.query_db import Query_db
from db.db_with_orm import Query_Db

class ActionGiveSchedule(Action):

    def name(self) -> Text:
        return "action_give_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(tracker.get_slot("section"))    
        print(tracker.get_slot("group"))
        # print(tracker.get_slot("group"))
        # print("AAAAAAAAAAAAAA")
        # # result=list(filter(lambda item: self.get_schedule(item, (tracker.get_slot("section"),tracker.get_slot("group"))),Database().select()))
        # # print (result)
        print(Query_db.retrieve_record_name_room(str(tracker.get_slot("section")),str(tracker.get_slot("group"))))
        dispatcher.utter_message("OK " + str(tracker.get_slot("section")) + str(tracker.get_slot("group")))

       

        return []
    

class ActionGiveHour(Action):

    def name(self) -> Text:
        return "action_give_hour"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # result=list(filter(lambda item: self.get_schedule(item, (tracker.get_slot("section"),tracker.get_slot("group"))),Database().select()))
        # print (result)
        now = datetime.datetime.now()
        print("fff")
        print(now.year, now.month, now.day, now.hour, now.minute, now.second)
        print(tracker.get_slot("group"))

        print(Query_Db.retrieve_name_room(self,section_="M1",grp_="alternant",time_="08:00"))
        # dispatcher.utter_message("Il est " + str(now.hour) + " heure")
        print(tracker.get_slot("section"))    
        print(tracker.get_slot("group"))
        # print(tracker.get_slot("group"))
        # print("AAAAAAAAAAAAAA")
        # # result=list(filter(lambda item: self.get_schedule(item, (tracker.get_slot("section"),tracker.get_slot("group"))),Database().select()))
        # # print (result)
        # dispatcher.utter_message(Query_Db.retrieve_schedule_halfday(self=self,section_="M2",grp_="classique",time_=str(now.hour)+":"+str(now.minute)))
        dispatcher.utter_message(Query_Db.retrieve_schedule_halfday(self=self,section_=tracker.get_slot("section"),grp_=tracker.get_slot("group"),time_=str(now.hour) + ":" + str(now.minute)))


        return []

class ActionGiveEmptyClass(Action):

    def name(self) -> Text:
        return "action_give_empty_class"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("test")
        print("section",tracker.get_slot("section"))
        print("group",tracker.get_slot("group"))
        print("time",tracker.get_slot("time"))


        dispatcher.utter_message(text=f'Ok')

        return []