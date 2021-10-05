-- SOURCE C:/path/data.sql;


USE pizzadatabase;

INSERT INTO restaurant_pizza VALUES 
    (1, 'Margarita'),
    (2, 'Meat Lovers'),
    (3, 'Hawaii'),
    (4, 'Spicy sausage'),
    (5, 'Vegetarian Lovers'),
    (6, 'Napolitana'),
    (7, 'Peperoni'),
    (8, 'Spicy salami'),
    (9, '4 chesses'),
    (10, 'Calzone')

; 
INSERT INTO restaurant_topping VALUES 
    (1, 'cheese', 2, true),
    (2, 'ham', 3, false),
    (3, 'tomatos', 0.5, true),
    (4, 'base', 1, true),
    (5, 'pinaple', 2, true),
    (6, 'vegetables in season', 3, true),
    (7, 'peperoni', 3, false),
    (8, 'salami', 4, false),
    (9, 'chillies', 1, true),
    (10, 'different chesses', 5, true)

;
INSERT INTO restaurant_pizza_toppings VALUES  
    (pizza_topping_id= 1 ,pizza_id= 1 , topping_id =4 )
    (pizza_topping_id= 2,pizza_id= 1, topping_id = 1)
    (pizza_topping_id= 3,pizza_id= 1, topping_id = 3)
    (pizza_topping_id= 4,pizza_id= 2 , topping_id= 4)
    (pizza_topping_id= 5,pizza_id= 2, topping_id=7 )
    (pizza_topping_id= 6,pizza_id= 2, topping_id=8 )
    (pizza_topping_id= 7,pizza_id= 3, topping_id=4 )
    (pizza_topping_id= 8,pizza_id= 3, topping_id= 5 )
    (pizza_topping_id= 9,pizza_id= 3, topping_id =1)
    (pizza_topping_id= 10,pizza_id= 4, topping_id=4 )
    (pizza_topping_id= 11,pizza_id= 4, topping_id=8 )
    (pizza_topping_id= 12,pizza_id= 4, topping_id=9 )
    (pizza_topping_id= 13,pizza_id= 5, topping_id=4 )
    (pizza_topping_id= 14,pizza_id= 5, topping_id= 6 )
    (pizza_topping_id= 15,pizza_id= 5, topping_id= 1 )
    (pizza_topping_id= 16,pizza_id= 6, topping_id =4)
    (pizza_topping_id= 17,pizza_id= 6, topping_id= 8 )
    (pizza_topping_id= 18,pizza_id= 6, topping_id= 3 )
    (pizza_topping_id= 19,pizza_id= 7, topping_id = 4)
    (pizza_topping_id= 20,pizza_id= 7, topping_id = 3 )
    (pizza_topping_id= 21,pizza_id= 7, topping_id= 7 )
    (pizza_topping_id= 22,pizza_id= 8, topping_id=4 )
    (pizza_topping_id= 23,pizza_id= 8, topping_id=8 )
    (pizza_topping_id= 24,pizza_id= 8, topping_id=9 )
    (pizza_topping_id= 25,pizza_id= 8, topping_id=1 )
    (pizza_topping_id= 26,pizza_id= 9, topping_id=4 )
    (pizza_topping_id= 27,pizza_id= 9, topping_id=10 )
    (pizza_topping_id= 28,pizza_id= 9, topping_id=6 )
    (pizza_topping_id= 29,pizza_id= 10, topping_id=4 )
    (pizza_topping_id= 30,pizza_id= 10, topping_id=2 )
    (pizza_topping_id= 31,pizza_id= 10, topping_id=3 )

    (3, 2, 1),
    (4, 2, 2),
    (5, 2, 3),
    (4, 2, 4),
    (6, 3, 1),
    (7, 3, 2),
    (8, 3, 3)

;
INSERT INTO restaurant_drink VALUES 
    (1, 'CocaCola', 3),
    (2, 'SevenUp', 3),
    (3, 'Fanta', 3),
    (4, 'Sparkling Water', 4)
;
INSERT INTO restaurant_desert VALUES 
    (1, 'Tiramisu', 4),
    (2, 'Chocolate lava cake', 5)
;
INSERT INTO restaurant_employee VALUES 
#ASSUMING MAASTRICHT are 56-62 
    (1, 'Mischa', 'Rauch', '56', 'Free'),
    (2, 'Lou', 'Rauch', '57', 'Free'),
    (3, 'Meli', 'Carioni', '58', 'Free'),
    (4, 'Marie', 'bersia', '59', 'Free'),
    (5, 'Adrien', 'bersia', '60', 'Free'),
    (6, 'Oscar', 'bersia', '61', 'Free'), 
    (7, 'Tom', 'Rauch', '62', 'Free'),
    (8, 'Ollie', 'Rauch', '56', 'Free'),
    (9, 'Alex', 'Carioni', '57', 'Free'),
    (10, 'Bianca', 'bersia', '58', 'Free'),
    (11, 'Marie', 'bersia', '59', 'Free'),
    (12, 'Spencer', 'bersia', '60', 'Free'), 
    (13, 'Simon', 'bersia', '61', 'Free'), 
    (14, 'Konstantine', 'bersia', '62', 'Free')
;

INSERT INTO restaurant_address VALUES 
#address_id, posta_code, coutry, street, house_number, city
(1, '6211RV', 'netherlands', 'capucijengag', '22', 'maastricht')
;

INSERT INTO restaurant_customer VALUES 
#id, name, last_name, email_Address, phone_number, discount_available, address_id 
(1, 'meli', 'carioni', 'carioni.rosamelia@gmail.com', 1234, false, 1)
; 
