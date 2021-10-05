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
    (1 ,  1 ,  4 ),
    (2,  1,   1),
    (3,  1,   3),
    (4,  2 ,    4),
    (5,  2,   7 ),
    (6,  2,   8 ),
    (7,  3,   4 ),
    (8,  3,    5 ),
    (9,  3,  1),
    (10,  4,   4 ),
    (11,  4,   8 ),
    (12,  4,   9 ),
    (13,  5,   4 ),
    (14,  5,    6 ),
    (15,  5,    1 ),
    (16,  6,  4),
    (17,  6,    8 ),
    (18,  6,    3 ),
    (19,  7,   4),
    (20,  7,   3 ),
    (21,  7,    7 ),
    (22,  8,   4 ),
    (23,  8,   8 ),
    (24,  8,   9 ),
    (25,  8,   1 ),
    (26,  9,   4 ),
    (27,  9,   10 ),
    (28,  9,   6 ),
    (29,  10,   4 ),
    (30,  10,   2 ),
    (31,  10,   3 )

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
    (7, 'Tom', 'Rauch', '62', 'Free')

;

INSERT INTO restaurant_address VALUES 
#address_id, posta_code, coutry, street, house_number, city
(1, '6211RV', 'netherlands', 'capucijengag', '22', 'maastricht'),
(2, '5611RV', 'netherlands', 'capucijengag', '22', 'maastricht'),
(3, '5711RV', 'netherlands', 'capucijengag', '22', 'maastricht'),
(4, '5811RV', 'netherlands', 'capucijengag', '22', 'maastricht'),
(5, '5911RV', 'netherlands', 'capucijengag', '22', 'maastricht')
;

INSERT INTO restaurant_customer VALUES 
#id, name, last_name, email_Address, phone_number, discount_available, address_id 
(1, 'meli', 'carioni', 'carioni.rosamelia@gmail.com', 1234, false, 1),
(2, 'meli', 'carioni', 'carioni.rosamelia@gmail.com', 1234, false, 2),
(3, 'meli', 'carioni', 'carioni.rosamelia@gmail.com', 1234, false, 3),
(4, 'meli', 'carioni', 'carioni.rosamelia@gmail.com', 1234, false, 4),
(5, 'meli', 'carioni', 'carioni.rosamelia@gmail.com', 1234, false, 5)
; 
