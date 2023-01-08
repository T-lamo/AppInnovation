# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
import datetime
from dateutil import parser
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet

from rasa_sdk.executor import CollectingDispatcher
import requests
from twilio.rest import Client

from geotext import GeoText




# from db.database import Database
# from db.query_db import Query_db
from db.db_with_orm import Query_Db
from socialisation.weather import getWeather
from socialisation.index import SociabilityQuestion
    
sociability=SociabilityQuestion()

class ActionGiveSchedule(Action):

    def name(self) -> Text:
        return "action_give_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        now = datetime.datetime.now()
        
        dispatcher.utter_message(Query_Db.retrieve_schedule_halfday(self=self,
            section_ = str(tracker.get_slot("section")).lower(),grp_ = str(tracker.get_slot("group")).lower(),time_=str(now.hour) + ":" + str(now.minute)))
        return []

class ActionGiveEmptyClass(Action):

    def name(self) -> Text:
        return "action_give_empty_class"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

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

        text = tracker.get_slot("city")
        text=str(text).title() 
        print("upper txt", text)
        # print("city info",tracker.get_slot("city"))
        places = GeoText(text)
        cities = places.cities
        print(places, cities, places.countries)
        # Output: ['England', 'France']

        # city = tracker.get_slot(cities[0])
        dispatcher.utter_message(getWeather(cities[0]))
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

class ActionJoke(Action):
    def name(self) -> Text:
        return "action_joke"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = "https://blague.xyz/api/joke/random"
        headers = { "Accept": "application/json" }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            joke = response.json()["joke"]
            dispatcher.utter_message(str(joke["question"]) +" "+ str(joke["answer"]))
        else:
            dispatcher.utter_message("Pas de blagues pour aujourd'hui")
        
        return []

class ActionSMS(Action):
    def name(self) -> Text:
        return "action_SMS"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phone = Query_Db.retrieve_prof_phone_by_name(self=self,name_ = str(tracker.get_slot("profName")).lower())
        print(tracker.get_slot("profName"),tracker.get_slot("profMessage"))
        account_sid = "AC64c34eb4c59c3febc79e26819d37a1df"
        auth_token = "ad15ba5285d7f558cd87cc5a5ef9b60d"
        twilio_phone_number = "+15153688407"

        client = Client(account_sid, auth_token)

        client.messages.create(
            from_=twilio_phone_number,
            to=phone,
            body= str(tracker.get_slot("profMessage"))
        )
        dispatcher.utter_message("Message envoyé !")
        
        return []

