# Project 2 - My Fashion Clothing Ecommerce

This document will serve as a guide for using our ecommerce website
via both an administartor and a user.

## Getting started

To use the ecommerce site, first navigate to http://localhost:8000
(this allows you to access the server that's been set up on your 
local machine via the README.md file instructions). This will also take
you to the home page. 

## Creating an account

In order to order items, you must have
created an account and registered with our system. To do that: 

* first navigate to the "Sign Up" link in the navigation bar atop the home 
page (this nav bar is also available throughout the site!). 

* Once there, please enter your custom username, a valid email address, and a password of your choosing 
in the appropriate fields and click "Sign Up"!

* Once your account has been successfully created, you will be redirected to 
the Login page. 

## Logging In
---

If you have just created an account, you will have been redirected to the Login page. If not, you can access it by clicking "Login" on the nav bar at the top of 
the site.

* Enter your username, email address, and password associated with your account.
* Select the "Login" button

It's that simple! If your information was entered correctly, and you have an
account, you will be logged in and redirected to your User Information page.

If you are already logged in, the "Login" on the nav bar will be replaced with your username and user level.

## User Information
---

If you are already logged in, you may access your User Information page by 
selecting "User: your_username" from the nav bar at the top of the site. All information associated with your account (except, of course, your password!) will be displayed, including:
* Username
* Email
* Type
* Active

## Product Search
In order to search for a product on the site, you must navigate to the products/all page by clicking on the "Product" on the
nav bar at the top of the site.

Once there you are able to filter the product by category and the size of the product. Select the options from the category and size you 
wish to view and click on the "Apply filters" button to view the filtered search.

## Order Product
Once you have found an item you would like to order, click on the "ADD TO CART" button next to the item being ordered.
This will bring you to the cart/fetch_user_cart page, where you are able:

* Change the quantity of items being ordered in your cart by changing the number in the text box to your desired amount
and clicking on the button "Confirm" to save the change to your cart. 
* Remove items from your cart by clicking on the "x" in the top-right corner of the item in your cart.

Once you wish to order your items, you must click on the "Checkout" button on the bottom of the page.

This will bring you to the orders/all page, where you will be able to view your previous orders associated with 
only your user account and their total costs.





## Administrator Functionalities

Login in superuser at http://127.0.0.1:8000/admin or the location address that Django provides after python manage.py runserver + /admin at the end using the username and password generated in step 6 of the Readme.md file.

By following step 6 of Readme.md, you will get
```
Username: joe
Password: 123
```
After logining in the adminstration site, superusers are permitted to edit or delete items in both CART and ORDERS, create new user accounts, or edit and delete items in PRODUCT. ("add items" of PRODUCT is abandoned.)

*NOTICE: administrator and user cannot login in the system at the same time. If administrator has logged in the administration's system, the out system will display the superuser that has logged in. If you want to switch from a super user to a normal user, please make sure to log out of the super user before logging in as a normal user.
<p>&nbsp;</p>




