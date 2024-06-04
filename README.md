# Online Shopping Website using Python-Django

![](https://github.com/Online_Shopping_Website_using_Python-Django/addidas.gif)

## Description
This project is an online shopping website developed using Python and the Django framework. It aims to provide users with a seamless online shopping experience, including browsing products, adding items to a cart, and managing orders.

## Features
- User authentication (login, signup, logout)
- Product listing and detail view
- Shopping cart functionality
- Order management
- Admin panel for managing products and orders

## Installation

### Prerequisites
- Python 3.x
- Django 3.x
- Virtualenv

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/DeathStar1711/Online_Shopping_Website_using_Python-Django.git
2. Navigate to the project directory:
    ```bash
    cd Online_Shopping_Website_using_Python-Django
3. Create a virtual environment:
    ```bash
    python -m venv env    
4. Activate the virtual environment:
    - On Windows:
      ```bash
      .\env\Scripts\activate
    - On macOS/Linux:
      ```bash
      source env/bin/activate
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
6. Apply migrations:
    ```bash
    python manage.py migrate
7. Create a superuser for the admin panel:
    ```bash
    python manage.py createsuperuser
8. Run the development server:
    ```bash
    python manage.py runserver
    
## Usage
1. Open your web browser and go to http://127.0.0.1:8000/
2. Register a new user or log in with an existing account.
3. Browse products, add items to your cart, and proceed to checkout.

## Project Structure
- DhamaWebsite/: Main application directory
- templates/: HTML templates
- static/: Static files (CSS, JavaScript, images)
- manage.py: Django's command-line utility

## Contributing
Contributions are welcome! Please create a pull request with a detailed description of your changes.
