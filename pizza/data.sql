-- SOURCE C:/path/data.sql;


USE pizzadatabase;

INSERT INTO restaurant_pizza VALUES 
    (1, 'Margaritha'),
    (2, 'Meat Lovers'),
    (3, 'Hawaii')
; 
INSERT INTO restaurant_topping VALUES 
    (1, 'cheese', 2, true),
    (2, 'ham', 4, false),
    (3, 'tomateos', 1, true)
;
INSERT INTO restaurant_pizza_toppings VALUES  
#pizza_topping_id, pizza_id, topping_id 
    (1, 1, 1),
    (2, 1, 3),
    (3, 2, 1),
    (4, 2, 2),
    (5, 2, 3),
    (6, 3, 1),
    (7, 3, 2),
    (8, 3, 3)

;
INSERT INTO restaurant_drink VALUES 
    (1, 'CocaCola', 3),
    (2, 'SevenUp', 3),
    (3, 'Fanta', 3),
    (4, 'Water', 4)
;
INSERT INTO restaurant_desert VALUES 
    (1, 'Teramisu', 4),
    (2, 'cor don blue', 3),
    (3, 'choclate lava cake', 5)
;
INSERT INTO restaurant_employee VALUES 
#ASSUMING MAASTRICHT are 56-62 
    (1, 'Mischa', 'Rauch', '56'),
    (2, 'Lou', 'Rauch', '57'),
    (3, 'Meli', 'Carioni', '59'),
    (4, 'Marie', 'bersia', '60'),
    (5, 'Adrien', 'bersia', '61'),
    (6, 'Kai', 'bersia', '62')
;

INSERT INTO restaurant_address VALUES 
#address_id, posta_code, coutry, street, house_number, cty

(1, '6211RV', 'netherlands', 'capucijengag', '22', 'maastricht')
;

INSERT INTO restaurant_customer VALUES 
#id, name, last_name, email_Address, phone_number, discount_available, address_id 
(1, 'meli', 'carioni', 'carioni.rosamelia@gmail.com', 1234, false, 1)
; 
