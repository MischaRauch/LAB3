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
    (1, 'Mischa', 'Rauch', '6217'),
    (2, 'Meli', 'Carioni', '5432'),
    (3, 'adrien', 'bersia', '234')
;

