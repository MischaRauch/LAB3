# -*- coding: utf-8 -*-
import re
from PyInquirer import prompt
import requests
import json
from pprint import pprint

from requests.api import request

BASE_URL = "http://localhost:8000"

main_list = {
    "type": "list",
    "name": "choice",
    "message": "What do you want to do?",
    "choices": ["Display Menu Pizza", "Display Menu Drinks", "Display Menu Deserts", "Create a user", "Login", "Get a user", "Quit"],
}


login_questions = [
    {"type": "input", "message": "Enter your username", "name": "username"},
    {"type": "password", "message": "Enter your password", "name": "password"},
]

create_questions = login_questions + [
    {"type": "input", "message": "Enter your e-mail address", "name": "email"},
]

user_id_questions = [
    {"type": "input", "message": "Enter the id", "name": "user_id"},
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


def login(username, password):
    response = requests.post(BASE_URL + "/login", data={"username": username, "password": password})
    print(response.json())


def create_user(postal_code, country, street, house_number, city, first_name, last_name, email, phone):
    response = requests.post(BASE_URL + "/createCustomer", data={"postal_code": postal_code, "country": country, "street": street, "house_number": house_number, "city": city, "first_name": first_name, "last_name": last_name, "email": email, "phone": phone})
    #answer_dict = json.loads(response.json())
    #print(answer_dict)


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
            pprint('This Pizza is Vegan')
        else:
            pprint('This pizza is not Vegan')
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

if __name__ == "__main__":
    while True:
        answers = prompt(main_list)
        answer = answers["choice"]
        if answer == "Create a user":
            create_answers = prompt(create_user_questions)
            create_user(**create_answers)
        if answer == "Login":
            login_answers = prompt(login_questions)
            login(**login_answers)
        if answer == "Get a user":
            get_user_answers = prompt(user_id_questions)
            get_user(**get_user_answers)
        if answer == "Quit":
            break
        if answer == "Display Menu Pizza":
            getsomething = get_menu()
        if answer == "Display Menu Drinks":
            getsomething = get_drinks()
        if answer == "Display Menu Deserts":
            getsomething = get_desserts()