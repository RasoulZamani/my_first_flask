# my_first_flask
## Description
This is my first flask restful project using SQLAlchemy, flask_jwt(-extended) based on Jose Course. It can create differernt stores with diverse items and each of them has name, price and id. also it has a login and register part. after creating acount (its free!) you can create your objects by post and update them by put methods. getting all or one special item or store is possible too, notice for posting it need authentication. it was tested by Postman. everything was OK. 

besises, I implement **dockerized** simple app [here](./dockerized_flask)

## Dependencies
aniso8601==9.0.1,
click==8.0.4,
Flask-RESTful==0.3.9,
Flask-SQLAlchemy==2.5.1,
greenlet==1.1.2,
itsdangerous==2.1.2,
Jinja2==3.1.1,
MarkupSafe==2.1.1,
PyJWT==1.4.2,
pytz==2022.1,
six==1.16.0,
SQLAlchemy==1.4.32,
Werkzeug==2.0.3,


## runnig
for using in root just run app.py:
```
python app.py
```
