# -*- coding: utf-8 -*-
import re
from PyInquirer import prompt
import requests
import json
import time 
from pprint import pprint

from requests.api import request

BASE_URL = "http://localhost:8000"

main_list = {
    "type": "list",
    "name": "choice",
    "message": "What do you want to do?",
    "choices": ["Display Menu Pizza", "Display Menu Drinks", "Display Menu Deserts", "Are you new?", "Login with customer_id", "Quit"],
}
sub_list = {
    "type": "list",
    "name": "choice",
    "message": "What do you want to do?",
    "choices": ["Add Pizza", "Add Drink", "Add Desert", "Quit"],
}


login_id = [
    {"type": "input", "message": "Enter your customer_id", "name": "customer_id"},
]

create_pizzaID_input =  [
    {"type": "input", "message": "Enter the pizza ID", "name": "pizza_id"},
    {"type": "input", "message": "Enter the quantity", "name": "quantity"},
]
create_drinkID_input =  [
    {"type": "input", "message": "Enter the drink ID", "name": "drink_id"},
    {"type": "input", "message": "Enter the quantity", "name": "quantity"},
]
create_desertID_input =  [
    {"type": "input", "message": "Enter the desert ID", "name": "desert_id"},
    {"type": "input", "message": "Enter the quantity", "name": "quantity"},
]


#postal_code, country, street, house_number, city, first_name, last_name, email, phone
create_user_questions = [
    {"type": "input", "message": "Enter your postal_code", "name": "postal_code"},
    {"type": "input", "message": "Enter your country", "name": "country"},
    {"type": "input", "message": "Enter your street", "name": "street"},
    {"type": "input", "message": "Enter your house_number", "name": "house_number"},
    {"type": "input", "message": "Enter your city", "name": "city"},
    {"type": "input", "message": "Enter your first_name", "name": "first_name"},
    {"type": "input", "message": "Enter your last_name", "name": "last_name"},
    {"type": "input", "message": "Enter your email", "name": "email"},
    {"type": "input", "message": "Enter your phone", "name": "phone"},
]


def login(customer_id):
    response = requests.post(BASE_URL + "/login", data={"customer_id": customer_id})
    sub_selection()
    #print(response.json())


def create_user(postal_code, country, street, house_number, city, first_name, last_name, email, phone):
    response = requests.post(BASE_URL + "/createCustomer", data={"postal_code": postal_code, "country": country, "street": street, "house_number": house_number, "city": city, "first_name": first_name, "last_name": last_name, "email": email, "phone": phone})
    sub_selection()
    #answer_dict = json.loads(response.json())
    #print(answer_dict)

def add_pizza(pizza_id, quantity):
    response = requests.post(BASE_URL + "/createOrderItem", data={"pizza_id": pizza_id, "quantity": quantity, "drink_id": 9999, "desert_id": 9999})
    sub_selection()

def add_drink(drink_id, quantity):
    response = requests.post(BASE_URL + "/createOrderItem", data={"pizza_id": 9999, "quantity": quantity, "drink_id": drink_id, "desert_id": 9999})
    sub_selection()

def add_desert(desert_id, quantity):
    response = requests.post(BASE_URL + "/createOrderItem", data={"pizza_id": 9999, "quantity": quantity, "drink_id": 9999, "desert_id": desert_id})
    sub_selection()

def get_user(user_id):
    response = requests.get(BASE_URL + "/user/" + user_id)
    print(response.json())

def get_menu():
    print("TEST:  ",BASE_URL)
    response = requests.get(BASE_URL)
    piz_dict = json.loads(response.json())
    index = 0
    while index < len(piz_dict):
        print('Pizza: ', index+1)
        pprint(piz_dict[index].get('fields').get('pizza_name'))
        veggi_request = requests.get(BASE_URL + "/veggi/" + str(index+1))
        veggi = json.loads(veggi_request.json())
        if (veggi):
            pprint('This Pizza is Vegeterian.')
        else:
            pprint('This pizza is not Vegeterian.')
        sub_response = requests.get(BASE_URL + "/"+ str(index+1))
        toppings = json.loads(sub_response.json())
        pprint(toppings)
        print()
        index = index +1

def get_drinks():
    response = requests.get(BASE_URL + "/drinks") 
    drinks_dict = json.loads(response.json())
    index = 0
    while index < len(drinks_dict):
        print('Drink: ', index+1)
        drink_name = drinks_dict[index].get('fields').get('drink_name')
        drink_price = requests.get(BASE_URL + "/drinks/" + str(index+1))
        #print("querey ",get_price)
        price = json.loads(drink_price.json())
        print('\t',drink_name, price)
        index = index +1 

def get_desserts():
    response = requests.get(BASE_URL + "/deserts") 
    desert_dict = json.loads(response.json())
    index = 0
    while index < len(desert_dict):
        print('Desert: ', index+1)
        desert_name = desert_dict[index].get('fields').get('desert_name')
        desert_price = requests.get(BASE_URL + "/desert/" + str(index+1))
        #print("querey ",get_price)
        price = json.loads(desert_price.json())
        print('\t',desert_name, price)
        index = index +1 

def sub_selection():
    while True:
        answers = prompt(sub_list)
        answer = answers["choice"]
        if answer == "Add Pizza":
            get_pizzaID = prompt(create_pizzaID_input)
            add_pizza(**get_pizzaID)
        if answer == "Add Drink":
            get_drinkID = prompt(create_drinkID_input)
            add_drink(**get_drinkID)
        if answer == "Add Desert":
            get_desertID = prompt(create_desertID_input)
            add_desert(**get_desertID)    
        if answer == "Quit":
            break

if __name__ == "__main__":
    
    while True:
        answers = prompt(main_list)
        answer = answers["choice"]
        if answer == "Are you new?":
            create_answers = prompt(create_user_questions)
            create_user(**create_answers)
        if answer == "Login with customer_id":
            login_answers = prompt(login_id)
            login(**login_answers)
        if answer == "Quit":
            break
        if answer == "Display Menu Pizza":
            getsomething = get_menu()
        if answer == "Display Menu Drinks":
            getsomething = get_drinks()
        if answer == "Display Menu Deserts":
            getsomething = get_desserts()

def check_time():
    current_time = time.gmtime()[4]
    while (True):
        time.sleep(60)
        #get all deliveries and for each, check if their status needs updating 
        response = requests.get(BASE_URL + "/orders")
        orders_dict = json.loads(response.json())
        index = 0
        while index < len(orders_dict):
            if (orders_dict[index].get('fields').get('order_time').time() - current_time)  > (60*5):
                #and status == Preparation then
                # change status to -> "on the way" and set employee -> "On delivery"
            elif (orders_dict[index].get('fields').get('order_time').time() - current_time)  > (60*15):
                #and status == On delivery 
                #change status to -> "Received" 
            elif (orders_dict[index].get('fields').get('order_time').time() - current_time)  > (60*15):
                
            



def thread_function():
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)