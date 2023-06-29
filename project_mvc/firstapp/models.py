from django.db import models

# Create your models here.

class Motos(models.Model):
    m_marca=models.CharField(max_length=50)
    m_modelo=models.CharField(max_length=50)
    m_year=models.IntegerField()
    m_est=models.CharField(max_length=10)
    
class Autos(models.Model):
    a_marca=models.CharField(max_length=50)
    a_modelo=models.CharField(max_length=50)
    a_year=models.IntegerField()
    a_est=models.CharField(max_length=10)

class Users(models.Model):
    user_name=models.CharField(max_length=50)
    user_pass=models.CharField(max_length=50)
    user_mail=models.EmailField()
    user_age=models.IntegerField()
    user_est=models.CharField(max_length=10)