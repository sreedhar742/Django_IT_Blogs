# Django IT Blogs

Welcome to **Django IT Blogs**! Here you can create an account, write blogs, and read other blogs.

---

## Setup Instructions

### 1. Create `.env` File
In the main project directory, create a `.env` file and provide the following details:

1. DB_NAME=your_db_name
2. DB_USER=your_db_user
3. DB_PASSWORD=your_db_password
4. DB_HOST=localhost
6. DB_PORT=3306

EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_passkey
---

## Start the Application

Follow these steps to get the application running:

### Install the Dependencies
```bash
step 1: install the modules
pip install -r requirements.txt

Step 2: Prepare for Migrations
python manage.py makemigrations

Step 3: Create the Database Tables
python manage.py migrate

Step 4: Start the Development Server
python manage.py runserver

The default development server runs at: http://127.0.0.1:8000/
If you want to use a different port, specify it like this:
python manage.py runserver <your_port_number>

