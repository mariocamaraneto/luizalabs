# Django Coding Test
The purpose of this coding test is to evaluate your skills using Python and the Django web
framework.
## The Problem
Luizalabs' team is growing every month and now we need to have some application to manage
employees' information, such as name, e-mail and department. As any application written at
Luizalabs, it must have an API to allow integrations.
### Deliverables
"Luizalabs Employee Manager" app must have:

● A Django Admin panel to manage employees' data

● An API to list, add and remove employees


## Install
- Clone the repository.

- Create virtual env and install requirements
```
python -m venv myvenv
source myvenv/bin/activate
pip install -r requirement.txt
```

- Migrate and create superuser
```
python manage.py migrate
python manage.py createsuperuser
```

- Run development server in localhost (default:http://localhost:8000)
```
python manage.py runserver
```

*You can test and see the deploy application in
[this link](http://labs.mariocn.com.br)*

## Usage
### API
You can use API in your web browser with forms or with cURL
* List employees
```
curl -H "Content-Type: application/json" http://labs.mariocn.com.br/employee/
```
* Retrieve an employee
```
curl -H "Content-Type: application/json" http://labs.mariocn.com.br/employee/1/
```
* Delete an employee
```
curl -X DELETE http://labs.mariocn.com.br/employee/1/
```
* Add new employee
```
curl -H "Content-Type: application/json" -X POST -d '{"name":"Mario Camara", "email":"mariocamaraneto@gmail.com", "departament": "Labs"}' http://labs.mariocn.com.br/employee/
```

### Web Admin
Go to link: http://labs.mariocn.com.br/admin/

AdminUser: teste

Pass: testando123


I think that don't need more explanations.
