# Storefront
Storefront is an E-Commerce web application built using Django web framework and MySQL database.

# Links & API Endpoints
Home Page <https://dejibuy-prod.herokuapp.com/> <br>
Admin Page <https://dejibuy-prod.herokuapp.com/admin> <br>
Carts endpoint <https://dejibuy-prod.herokuapp.com/store/carts> <br>
Cart Items endpoint <https://dejibuy-prod.herokuapp.com/store/carts/> + id <br>
Products endpoint <https://dejibuy-prod.herokuapp.com/store/products> <br>
Product Item endpoint <https://dejibuy-prod.herokuapp.com/store/products/ + id  <br>
Product Item Reviews endpoint <https://dejibuy-prod.herokuapp.com/store/products/> + id + /reviews <br>
Product Item Review endpoint <https://dejibuy-prod.herokuapp.com/store/products/> + id + /reviews/ + id<br>
Product Item Images endpoint <https://dejibuy-prod.herokuapp.com/store/products/> + id + /images <br>
Collections endpoint <https://dejibuy-prod.herokuapp.com/store/collections> <br>
Collection Item endpoint <https://dejibuy-prod.herokuapp.com/store/collections/> + id  <br>
Orders endpoint <https://dejibuy-prod.herokuapp.com/store/orders> <br>
Order Items endpoint <https://dejibuy-prod.herokuapp.com/store/orders> <br>
Create user endpoint <https://dejibuy-prod.herokuapp.com/auth/users> <br>

## MySQL Command

Pass in the username as root and type in password
```bash
mysql -u root -p
```
## Populate Database
```bash
python manage.py seed_db
```

## Setup Fake SMTP Server
```bash
docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev
```
### SMTP Admin Panel
```bash
localhost:3000
```
## Run/Install redis
```bash
docker run -d -p 6379:6379
```
## Run celery worker
```bash
celery -A storefront worker --loglevel=info
```
## Schedule periodic celery tasks
```bash
celery -A storefront beat 
```
## Monitor celery tasks
```bash
celery -A storefront flower 
```
## Access Flower Admin Panel
```bash
localhost:5555
```