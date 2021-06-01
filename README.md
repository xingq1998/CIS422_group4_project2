# CIS422_group4_project2

Welcome to MyFashion Clothing Ecommerce

* Title: ReadME.md
* Project: MyFashion Clothing Ecommerce
* Team: NoMad
* Course Name: CIS 422
* Assignment: Project 2
* Date: May 31, 2021

# Architecture

The website consists of two parts:

* A public site that lets users browse and order products.
* An administrator ability.

# Environment

* Database: SQLite
* Website framework: django Python 3.7.9

# How to run

1) Open a shell program of your choice and change to the directory that contains the manage.py file.
2) You must have the django package installed on your local machine. You can tell django is installed and which version by running the following command.

    `$ python -m django --version`

3) The following command must be run if there is no version of django found.

    `$ pip install django`

4) Once django is installed, the database tables need to be created and synced by running the following commands:

    `$ python manage.py makemigrations`

    `$ python manage.py migrate`

5) Populate the database tables with test data by running:

    `$ python uploadTestData.py `

6) Create a superuser account (which will be an administrator of the site) by running:

    `$ python manage.py createsuperuser --username=joe --email=joe@example.com`

    Then provide a password such as 123 and authenticate it when prompted.
    Remember both the username and password as their use will be described in the UserGuide.md.

7) To run the Django project, run the following command in the shell prompt:

    `$ python manage.py runserver `

8) Finally, you will be able to use the website while the server is running. See UserGuide.md file for documentation on how to access and use the site.

8) Once you are done with the server, return to the shell where you enterd the previous commands and press ctrl+c to stop the local server from running.

### Finished functionalities by Xing

- Design and maintain CartItem, OrderItem and Order data models
- add Product to Shopping Cart
- Update Shopping Cart (create,mdf and delete cart items), update related product instance responsively
- Checkout
- Create and display user Orders

# Reference

For Django backend: https://docs.djangoproject.com/en/3.2
