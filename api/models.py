from django.db import models

# Create your models here.

class Collage(models.Model):
    collage_id= models.AutoField(primary_key=True)
    cname = models.CharField(max_length=50)
    cwebsite = models.CharField(max_length=50,unique=True)
    cAddress = models.CharField(max_length=100)
    cAffiliation = models.CharField(max_length=50)
    cabout= models.TextField()

    def __str__(self):
        return self.cname


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    roll_no = models.CharField(max_length=20,unique=True)
    sName = models.CharField(max_length=50)
    sEmail= models.CharField(max_length=50, unique=True)
    sAddress = models.CharField(max_length=100)
    sCourse = models.CharField(max_length=50)
    shighestqualification = models.CharField(max_length=15)
    collage = models.ForeignKey(Collage,on_delete=models.CASCADE ,default=1)

    def __str__(self):
        return self.sName