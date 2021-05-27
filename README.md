# CIS422_group4_project2

python manage.py runserver


### Finished functionalities by Xing

- Design and maintain CartItem, OrderItem and Order data models
- add Product to Shopping Cart
- Update Shopping Cart (create,mdf and delete cart items), update related product instance responsively
- Checkout
- Create and display user Orders

# update data model

```shell
python manage.py makemigrations
python manage.py migrate
```

## Admin:
Create superusers using the createsuperuser command:
```shell
~/mysite $ python manage.py createsuperuser --username=joe --email=joe@example.com
```
Then, setup password for superuser(administrator).
