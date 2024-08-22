import mysql.connector
from mysql.connector import Error
from .email_sent import send_email_via_gmail
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_mysql():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )

    if connection.is_connected():
        print("Connected to MySQL database")
    return connection
def car_models():
    connection = connect_to_mysql()
    cursor = connection.cursor()
    
    query = "SELECT car_model FROM car"
    
    cursor.execute(query)
    
    car_models = [model[0] for model in cursor.fetchall()]
    
    cursor.close()
    connection.close()
    
    return car_models

def car_price(car_model):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    
    query = "SELECT price FROM car WHERE car_model=%s"
    
    cursor.execute(query, (car_model,))

    
    prices = cursor.fetchone()

    cursor.close()
    connection.close()
    
    return prices

def book_appoitment(customer_name, employee_name, purpose, appointment_date,appointment_time):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    employee= "select employee_name from employee where employee_name=%s"
    cursor.execute(employee, (employee_name,))
    if employee:
        query = "INSERT INTO appointments (customer_name, employee_name, purpose, appointment_date,appointment_time) VALUES (%s, %s, %s, %s)"
        
        appointment = (customer_name, employee_name, purpose, appointment_date,appointment_time)
        
        cursor.execute(query, appointment)

        email = "SELECT email FROM employee WHERE employee_name=%s"
        cursor.execute(email, (employee_name,))
        cursor.fetchone()[0]
        send_email_via_gmail(email, 'Appointment Booking', 'f"Appointment Booking confirmed to discuss about {purpose} with {customer_name} on {appointment_data} at {appointment_time}')
        
        connection.commit()
        cursor.close()
        connection.close()
        message = "Appointment booked successfully"
    else:
        message=f"Employee not found"
    return message
def cancel_appointment(customer_name):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    query = "DELETE FROM customer WHERE customer_name=%s"
    appointment = (customer_name,)
    cursor.execute(query, appointment)
    connection.commit()
    cursor.close()
    connection.close()
    message = "Appointment cancelled successfully"
    return message

def reschedule_appointment(customer_name, new_date,new_time):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    query = "UPDATE customer SET appointment_date=%s, appointment_time=%s WHERE customer_name=%s"
    appointment = (new_date, new_time, customer_name)
    cursor.execute(query, appointment)
    connection.commit()
    cursor.close()
    connection.close()
    message = "Appointment rescheduled successfully"
    return message



if __name__ =="__main__":
    connect_to_mysql()
