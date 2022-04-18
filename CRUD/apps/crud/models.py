from django.db import models

# Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=125, help_text='Message Title.')
#     message = models.TextField(help_text='What is on your mind...')

#     def __str__(self):
#         return self.title

class Employee(models.Model):
    eid = models.CharField(max_length=30)
    ename = models.CharField(max_length=120)
    eemail= models.EmailField()
    econtact = models.CharField(max_length=20)

    def __str__(self):
        return self.ename