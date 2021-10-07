# -*- coding: utf-8 -*-
import re

from django.http import response
from PyInquirer import prompt
import requests
import json
import time 
from pprint import pprint
from datetime import datetime

from requests.api import request


BASE_URL = "http://localhost:8000"

main_list = {
    "type": "list",
    "name": "choice",
    "message": "What do you want to do?",
    "choices": ["Display Menu Pizza", "Display Menu Drinks", "Display Menu Deserts", "Are you new?", "Login with customer_id", "Cancel Order", "Get Order Info" ,"Quit"],
}
sub_list = {
    "type": "list",
    "name": "choice",
    "message": "Add Pizza",
    "choices": ["Add Pizza"],
}
sub_sub_list = {
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
create_orderID_input = [
    {"type": "input", "message": "Enter the order ID", "name": "order_id"},
]


#postal_code, country, street, house_number, city, first_name, last_name, email, phone
create_user_questions = [
    {"type": "input", "message": "Enter your postal_code (56-62)", "name": "postal_code"},
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
    if (response.status_code != 200):
        print ('All employees are busy. Try in 5 minutes. ')
        exit()
    else : 
        sub_selection()
       # print(response.json())


def create_user(postal_code, country, street, house_number, city, first_name, last_name, email, phone):
    response = requests.post(BASE_URL + "/createCustomer", data={"postal_code": postal_code, "country": country, "street": street, "house_number": house_number, "city": city, "first_name": first_name, "last_name": last_name, "email": email, "phone": phone})
    if (response.status_code != 200):
        print ('All employees are busy. Try in 5 minutes. ')
        exit()
    sub_selection()
    #answer_dict = json.loads(response.json())
    #print(answer_dict)

def add_pizza(pizza_id, quantity):
    response = requests.post(BASE_URL + "/createOrderItem", data={"pizza_id": pizza_id, "quantity": quantity, "drink_id": 9999, "desert_id": 9999})
    sub_sub_selection()

def add_drink(drink_id, quantity):
    response = requests.post(BASE_URL + "/createOrderItem", data={"pizza_id": 9999, "quantity": quantity, "drink_id": drink_id, "desert_id": 9999})
    sub_sub_selection()

def add_desert(desert_id, quantity):
    response = requests.post(BASE_URL + "/createOrderItem", data={"pizza_id": 9999, "quantity": quantity, "drink_id": 9999, "desert_id": desert_id})
    sub_sub_selection()

def get_user(user_id):
    response = requests.get(BASE_URL + "/user/" + user_id)
    print(response.json())

def create_cancel_order(order_id):
    response = requests.post(BASE_URL + "/cancelOrder", data={"order_id": order_id})

def create_order_info(order_id):
    response = requests.post(BASE_URL + "/orderinfo", data={"order_id": order_id})
    info = json.loads(response.json())
    print(info)

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

def show_order():
    response = requests.get(BASE_URL + "/showorder")
    order_dict = json.loads(response.json())
    response1 = requests.get(BASE_URL + "/deliveryestimation")
    responsee = json.loads(response1.json())
    for order in order_dict:
        if (order['pizza_id'] == None):
            del order['pizza_id']
        if (order['desert_id'] == None):
            del order['desert_id']
        if (order['drink_id'] == None):
            del order['drink_id']
    pprint(order_dict)
    pprint(responsee)

def sub_selection():
    while True:
        answers = prompt(sub_list)
        answer = answers["choice"]
        if answer == "Add Pizza":
            get_pizzaID = prompt(create_pizzaID_input)
            add_pizza(**get_pizzaID)
            break

def sub_sub_selection():
    while True:
        answers = prompt(sub_sub_list)
        answer = answers["choice"]
        if answer == "Add Pizza":
            get_pizzaID = prompt(create_pizzaID_input)
            add_pizza(**get_pizzaID)
            break
        if answer == "Add Drink":
            get_drinkID = prompt(create_drinkID_input)
            add_drink(**get_drinkID)
            break
        if answer == "Add Desert":
            get_desertID = prompt(create_desertID_input)
            add_desert(**get_desertID)    
            break
        if answer == "Quit":
            show_order()
            break

def check_time():
    update_order_status_of_order('Preparation', 'On the way', 60*5)
    update_order_status_of_order('On the way', 'Received by customer', 60*15)
    update_employee_status()

def update_order_status_of_order(old_status, new_status, time_diff):
    current_time = datetime.now()
    response = requests.get(f'{BASE_URL}/orders?status={old_status}')
    if(response == 200):
        orders_dict = json.loads(response.json())
        for ord in orders_dict:
            ord_time = datetime.strptime(ord.get('fields').get('order_time'), '%Y-%m-%dT%H:%M:%S.%f%z')
            ord_time = ord_time.replace(tzinfo=None)
            if ( current_time -  ord_time ).total_seconds()  > time_diff:
                post_res = requests.post(f'{BASE_URL}/orders/{ord.get("pk")}/', data={'new_status': new_status})

def update_employee_status():   
    response = requests.get(BASE_URL + "/updateEmployees") 



#TODO add option to display status of order
if __name__ == "__main__":
    while True:
        
        answers = prompt(main_list)
        answer = answers["choice"]
        if answer == "Are you new?":
            create_answers = prompt(create_user_questions)
            create_user(**create_answers)
            check_time()
        if answer == "Login with customer_id":
            login_answers = prompt(login_id)
            answer = login(**login_answers)
            check_time()
        if answer == "Cancel Order":
            order_id = prompt(create_orderID_input)
            create_cancel_order(**order_id)   
        if answer == "Get Order Info":
            order_id = prompt(create_orderID_input)
            create_order_info(**order_id)
        if answer == "Quit":
            break
        if answer == "Display Menu Pizza":
            getsomething = get_menu()
            check_time()
        if answer == "Display Menu Drinks":
            getsomething = get_drinks()
            check_time()
        if answer == "Display Menu Deserts":
            getsomething = get_desserts()
            check_time()
        
        