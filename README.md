# A simple real time chat application in Django

## Table of Contents

- [A simple real time chat application in Django](#a-simple-real-time-chat-application-in-django)
  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
  - [Technologies](#technologies)
  - [Set Up](#set-up)
  - [Usage](#usage)
  - [Going Further](#going-further)

## General Information

A simple realtime Chat Application in Python using Django

## Technologies

- Python
- Django

## Set Up

- Install Pip following this [instruction](https://pip.pypa.io/en/stable/installation/)
- Set up virtual environment following this [instruction](https://docs.python.org/3/library/venv.html)
- Clone [this repository](https://github.com/VincentNguyenDuc/realtime-chat-application.git) to your working directory
- Install dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

- Create a .env file in realchat folder, generate a random SECRET_KEY and copy paste into the .env file:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

```python
# within the .env file
SECRET_KEY = "{new secret key}"
```

## Usage

- To run the server, activate the virtual environment, and running the following command:

```bash
python manage.py runserver
```

## Going Further

- Have to secure "SECRET_KEY"
