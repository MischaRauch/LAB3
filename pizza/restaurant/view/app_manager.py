# -*- coding: utf-8 -*-
import re
from PyInquirer import prompt
import requests
import json
from pprint import pprint

BASE_URL = "http://localhost:8000"

main_list = {
    "type": "list",
    "name": "choice",
    "message": "What do you want to do?",
    "choices": ["Create a user", "Login", "Get a user", "Quit", "Get all Pizzas"],
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

def get_all_pizzas():
    print("TEST:  ",BASE_URL)
    response = requests.get(BASE_URL)
    piz_dict = json.loads(response.json())
    pprint(piz_dict )


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
        if answer == "Get all Pizzas":
            getsomething = get_all_pizzas()