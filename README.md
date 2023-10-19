# Pizza Delivery System with MySQL Database
## Maastricht University | Course: Databases

## [Demonstration Video](https://www.youtube.com/watch?v=0BGUbUTF7sU&ab_channel=MischaRauch)
Click on the link above to view a demonstration of the final product.

## Overview
This repository contains a Pizza delivery system backed by a MySQL database. The application is built using the Django framework, following the Model-View-Controller (MVC) architecture. Users can order pizzas and input their address via the terminal, and the data is subsequently stored in the database. This project was developed as a LAB for the Database course at Maastricht University.

## Features

1. **MySQL Database**: The application is integrated with a MySQL database, ensuring efficient data storage and retrieval for the pizza delivery system.
2. **Django Framework**: Built on the Django framework, the application benefits from its robustness and scalability.
3. **MVC Architecture**: The project follows the Model-View-Controller (MVC) design pattern, ensuring a clear separation of concerns.
4. **Terminal-based Ordering**: Users can place pizza orders and provide their address details directly from the terminal.
5. **Admin Interface**: The `admin.py` file provides functionalities for the Django admin interface.
6. **URL Routing**: The `urls.py` file defines the URL patterns for the application.
7. **Views & Templates**: The application uses Django's views and templates system. The `views.py` file contains the logic for handling user requests, while templates provide the structure for web pages.
8. **Models**: The `models.py` file defines the data models, representing entities like pizzas, toppings, orders, and addresses.
9. **Queries**: Custom database queries are present in the `queries.py` file.
10. **App Manager**: The `app_manager.py` file manages the different components of the application.

## Database Schema Visualization
The following image represents the schema of the database. This schema provides a graphical representation of the database structure, showcasing the relationships between different entities and how data is organized.

![SchemaDatabases](https://user-images.githubusercontent.com/51691839/205130367-a8202c48-0c9c-4395-b632-895c8a792573.png)

This visual aid is crucial for understanding the underlying database design, offering developers and collaborators a quick grasp of the project's structure.

## Setup & Installation

1. Clone the repository to your local machine.
2. Navigate to the `pizza` directory.
3. Run `manage.py` to start the Django development server.
4. Access the application on your browser using the provided URL or interact via the terminal for ordering.
