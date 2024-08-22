import smtplib
from email.mime.text import MIMEText
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from .db_conn import car_models, car_price, book_appoitment, cancel_appointment, reschedule_appointment

class ActionProvideCarModels(Action):
    def name(self) -> str:
        return "action_provide_car_models"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> list:
        models = car_models()
        message = f"We have the following car models available: {models}."
        dispatcher.utter_message(text=message)
        return []

class ActionProvidePrice(Action):
    def name(self) -> str:
        return "action_provide_price"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> list:
        car_model = tracker.get_slot('car_model')
        model = car_models()
        if car_model in model:
            price = car_price(car_model)
            message = f"The price of the {car_model} is {price}."
        else:
            message = "Sorry, I don't have information about that car model."
        dispatcher.utter_message(text=message)
        return []

class ActionBookAppointment(Action):
    def name(self) -> str:
        return "action_book_appointment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> list:
        customer_name = tracker.get_slot('customer_name')
        employee_name = tracker.get_slot('employee_name')
        purpose = tracker.get_slot('appointment_purpose')
        date = tracker.get_slot('appointment_date')
        time = tracker.get_slot('appointment_time')
        # Here, you would add code to save the appointment in a database or system
        message = book_appoitment(customer_name,employee_name,purpose,date,time)
        dispatcher.utter_message(text=message)
        return []

class ActionCancelAppointment(Action):
    def name(self) -> str:
        return "action_cancel_appointment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> list:
        customer_name = tracker.get_slot('customer_name')

        message=cancel_appointment()
        
        dispatcher.utter_message(text=message)
        return []

class ActionRescheduleAppointment(Action):
    def name(self) -> str:
        return "action_reschedule_appointment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> list:
        customer_name = tracker.get_slot('customer_name')
        new_date = tracker.get_slot('new_date')
        new_time = tracker.get_slot('new_time')
        message=reschedule_appointment(customer_name,new_date,new_time)
        dispatcher.utter_message(text=message)
        return []
