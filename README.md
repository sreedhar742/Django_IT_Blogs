# Django_IT_Blogs
Here you can create your account and write your blogs and read other blogs.
Create the .env file in the main project environment and provide the details
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_password

start the application:
step-1:
install the depedencies
pip install -r requirement.txt
step-2:
prepare for migrations
python mange.py makemigrations
step-3:
created the database tables
python manage.py migrate

Step 4: Start the Development Server
python manage.py runserver
<!-- if default runs on the http://127.0.0.1:8000/ and if you wish runs on the another port you mention the port number after runserver-->