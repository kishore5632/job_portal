from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class SignUp(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    contact = models.CharField(max_length=20)

class Joblist(models.Model):
    company = models.CharField(max_length=50)
    jobtitle = models.CharField(max_length=20)
    skills = models.CharField(max_length=20)
    vaccancy = models.CharField(max_length=20)

class Apply(models.Model):
    
    document = models.FileField(upload_to='media/documents', null=True, blank=True)

    
    # checking webhook for auto commits for jenkins.
