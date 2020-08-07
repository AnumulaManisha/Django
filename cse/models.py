from django.db import models

# Create your models here.
class Placement(models.Model):

    companyname = models.CharField(max_length=100)
    package = models.IntegerField(default=0)
    no_of_stud = models.IntegerField(default=0)

class Feedback(models.Model):
    userName = models.CharField(max_length=100)
    userEmail = models.EmailField()
    subject = models.CharField(max_length=50)
    content = models.TextField()

#class Tsignup(models.Model):
 #   email = models.EmailField()
  #  firstname = models.CharField(max_length=100)
    #lastname = models.CharField(max_length=100)
   # password1 = models.CharField(max_length=50)
    #password2 = models.CharField(max_length=50)
class ImagesUpload(models.Model):
    subject = models.CharField(max_length=50)
    semester = models.IntegerField(default=0)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/')