# TinyLife Wellness Backend


## Description
Welcome to the TinyLife Wellness Backend!
This is the backend logic for TinyLife Wellness, a product that predicts the risk level of lead exposure in Kenya. The backend of this project connects the machine learning model to the web portal.

## Table of Contents
- [Built With](#built-with)
- [Prerequisites](#prerequisites)
- [Installation](#installation)

### Built With
Django

### Prerequisites
- Python (Version 3.9)
- Python Package Manager (pip)


### Installation
To run this Django project locally, please follow these steps:
- Clone the repository:
  ```
  git clone https://github.com/akirachix/Neza-Backend.git
  ```
  
- Navigate to the project directory:
  ```
  cd Neza-Backend
  ```
  
- Create a virtual environment:
  ```
  python -m venv <your environment name>
  ```

- Activate the virtual environment:
  On Linux and macOS:
   ```
  python manage.py source <environment name>/bin/activate
  ```
  On Windows:
  ```
  <environment name>\scripts\activate
  ```
  
- Install requirements:
  ```
  pip install -r requirements.txt
  ```
  
- Apply migrations:
  ```
  python manage.py migrate
  ```
  
- Run the development server:
  ```
  python manage.py runserver
  ```

