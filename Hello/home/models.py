from django.db import models


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    date=models.DateField()
class Triund(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    person=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=10,null=True)
    date=models.CharField(max_length=10)


class Kareri(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    person=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=10,null=True)
    date=models.CharField(max_length=10)



class Thatharana(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    person=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=10,null=True)
    date=models.CharField(max_length=10)



class Himani(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    person=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=10,null=True)
    date=models.CharField(max_length=10)



    
class Indrahara(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    person=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=10,null=True)
    date=models.CharField(max_length=10)


    
class Rising(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    person=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=10,null=True)
    date=models.CharField(max_length=10)


class Laka(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    person=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=10,null=True)
    date=models.CharField(max_length=10)





    

    


    def __str__(self):
        return self.name
    def __str__(self):
        return self.name



