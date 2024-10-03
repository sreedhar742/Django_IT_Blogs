from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from .forms import UserRegisterForm
class Testcasedemo(TestCase):
    # def setUp(self):
    #     global username
    #     global password1
    #     global  email
    #     global password2
    
    # def test_register(self):
    #     form=UserRegisterForm(username="farooq",email="psreedhar742@gmail.com",password1="car@123@CAR",password2="car@123@CAR")
    #     form.save()
     
        
    def test_register(self):
        url=reverse('register')
        response=self.client.get(url)
        self.assertEquals(response.status_code,200)
        
    def test_login(self):
        url=reverse('login')
        response=self.client.get(url)
        self.assertEquals(response.status_code,200)
    
    
    
    
        