# Yatube v.0.2.0 Forms
Social network. 

## Features
- View Posts.

### New features
- Signup and login;
- View detail of post;
- Create posts;
- Update own posts.

## History of Yatube project
- v.0.2.0 [Forms] - <- You are here
- v.0.1.0 [Community] - Ability to view posts.

## Tech
- Python 3.9
- Django 2.2

#### Tested Python version
Python 3.7-3.9


## Installation (for Windows)
Clone repository
```sh
git clone git@github.com:KuzenkovAG/yatube_forms.git
```
Install environment
```sh
python -m venv venv
```
Activate environment
```sh
source venv/Script/activate
```
Install requirements
```sh
pip install -r requirements.txt
```
Make migrations and run server
```sh
python manage.py migrate
```
Run server
```sh
python manage.py runserver
```

## Usage
Index page
```sh
http://127.0.0.1:8000/
```

Page of post (if post with id=1 exists)
```sh
http://127.0.0.1:8000/posts/1/
```
Create post
```sh
http://127.0.0.1:8000/create/
```

Page of user_name (if user with username=user_name exists)
```sh
http://127.0.0.1:8000/profile/user_name/
```

Page of group (if group with slug=group_slug exists)
```sh
http://127.0.0.1:8000/group/group_slug/
```



## Author
[Alexey Kuzenkov]

   [PythonAnyWhere]: <https://alexey241390.pythonanywhere.com/>

   [Alexey Kuzenkov]: <https://github.com/KuzenkovAG>
   [Forms]: <https://github.com/KuzenkovAG/yatube_forms>
   [Community]: <https://github.com/KuzenkovAG/yatube_community>