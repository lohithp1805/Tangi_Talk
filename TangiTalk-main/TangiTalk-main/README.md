Chat app with Django and Django channels.

# Getting Started

## Project setup and run
#### Install [redis](https://github.com/tporadowski/redis/releases/download/v5.0.14.1/Redis-x64-5.0.14.1.msi). 

<div class="flex-container" style="display: flex;">
        <img src="https://drive.google.com/uc?id=1Hn81fClbq08hyjG6VypQ6eAwnx9lXtdu" alt="redis folder" style="width: 450px">
        <img src="https://drive.google.com/uc?id=11bEavO5DHfx6Qhd_KH8eIPqicrIVeQa9" alt="redis-cli" style="height: 300px">
    </div>
<br/>
 Setup the redis and open redis cli and run it backgorund for the first time

> Install dependency
```bash
pip install -r requirements.txt
```
> Migrate database and create superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```
> Run the server
```bash
python manage.py runserver
```

<br />

![alt text](/static/gifs/preview.gif)
