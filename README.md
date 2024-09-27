# Django IT Blogs

Welcome to **Django IT Blogs**! Here you can create an account, write blogs, and read other blogs.

---

## Setup Instructions

### 1. Create `.env` File
In the main project directory, create a `.env` file and provide the following details:

DB_NAME=your_db_name DB_USER=your_db_user DB_PASSWORD=your_db_password DB_HOST=localhost DB_PORT=3306

EMAIL_HOST_USER=your_email EMAIL_HOST_PASSWORD=your_password

yaml
Copy code

---

## Start the Application

Follow these steps to get the application running:

### Step 1: Install the Dependencies
```bash
pip install -r requirements.txt
Step 2: Prepare for Migrations
bash
Copy code
python manage.py makemigrations
Step 3: Create the Database Tables
bash
Copy code
python manage.py migrate
Step 4: Start the Development Server
bash
Copy code
python manage.py runserver
The default development server runs at: http://127.0.0.1:8000/
If you want to use a different port, specify it like this:

bash
Copy code
python manage.py runserver <your_port_number>
Features
Create and manage your blog posts
Read blogs from other users
User authentication (login, registration, password reset)
Responsive and user-friendly interface
Technologies Used
Backend: Django, Python
Database: MySQL
Frontend: HTML, CSS, JavaScript
Deployment: Docker, Gunicorn
