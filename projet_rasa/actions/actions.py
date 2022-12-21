# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import datetime
from dateutil import parser
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# from db.database import Database
# from db.query_db import Query_db
from db.db_with_orm import Query_Db
from socialisation.weather import getWeather
from socialisation.index import SociabilityQuestion

# class ActionGiveSchedule(Action):

#     def name(self) -> Text:
#         return "action_give_schedule"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         print(tracker.get_slot("section"))    
#         print(tracker.get_slot("group"))
#         # print(tracker.get_slot("group"))
#         # print("AAAAAAAAAAAAAA")
#         # # result=list(filter(lambda item: self.get_schedule(item, (tracker.get_slot("section"),tracker.get_slot("group"))),Database().select()))
#         # # print (result)
#         print(Query_Db.retrieve_record_name_room(str(tracker.get_slot("section")),str(tracker.get_slot("group"))))
#         dispatcher.utter_message("OK " + str(tracker.get_slot("section")) + str(tracker.get_slot("group")))

       

#         return []
    
sociability=SociabilityQuestion()
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

        # print(Query_Db.retrieve_name_room(self,section_="M1",grp_="alternant",time_="08:00"))
        # dispatcher.utter_message("Il est " + str(now.hour) + " heure")
        print(tracker.get_slot("section"))    
        print(tracker.get_slot("group"))
        # print(tracker.get_slot("group"))
        print("AAAAAAAAAAAAAA")
        # # result=list(filter(lambda item: self.get_schedule(item, (tracker.get_slot("section"),tracker.get_slot("group"))),Database().select()))
        # # print (result)
        # dispatcher.utter_message(Query_Db.retrieve_schedule_halfday(self=self,section_="M2",grp_="classique",time_=str(now.hour)+":"+str(now.minute)))
        dispatcher.utter_message(Query_Db.retrieve_schedule_halfday(self=self,
            section_ = str(tracker.get_slot("section")).lower(),grp_ = str(tracker.get_slot("group")).lower(),time_=str(now.hour) + ":" + str(now.minute)))


        return []

class ActionGiveEmptyClass(Action):

    def name(self) -> Text:
        return "action_give_empty_class"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("test")
        # print("time: ",tracker.get_slot("time"))
    
        # print("type: "+str(tracker.get_slot("time")))
        # (datetime.datetime.strptime(tracker.get_slot("time"), "%Y-%m-%dT%H:%M:%S.000-08:00")) #tracker.get_slot("time")
        #date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
        #2022-12-16T12:00:00.000-08:00
        datetime_slot_time = parser.parse(tracker.get_slot("time"))
        date_time_dispo = str(datetime_slot_time.year)+"-"+str(datetime_slot_time.month)+"-"+str(datetime_slot_time.day)
        print("time: "+str(datetime_slot_time.hour) +":"+str(datetime_slot_time.minute))
        print("date: "+ date_time_dispo)


        dispatcher.utter_message(Query_Db.retrieve_salle_disponible(self=self,
            date_ = (date_time_dispo), time_= str(datetime_slot_time.hour)+":"+str(datetime_slot_time.minute)))

        dispatcher.utter_message(text=f'Ok')

        return []


class ActionGiveWeather(Action):
    def name(self) -> Text:
        return "action_give_weather"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot("city")
        dispatcher.utter_message(getWeather(city))
        return []

class ActionGiveUnivInfo(Action):
    def name(self) -> Text:
        return "action_give_univ_info"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(sociability.univInfo())
        return []

class ActionGiveUnivHoraireAcceuil(Action):
    def name(self) -> Text:
        return "action_give_univ_horaire_acceuil"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(sociability.univHeureAcceuil())
        return []
class ActionGiveAddresseServiceAccompagnement(Action):
    def name(self) -> Text:
        return "action_give_addresse_service_accompagnement"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(sociability.ServiceAccompagement())
        return []