from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class owner_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    image=models.ImageField('images/',null=True)
    status= models.CharField(max_length=100,null=True)

class user_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    image=models.ImageField('images/',null=True)
    status= models.CharField(max_length=100,null=True)

class add_appartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50, null=True)
    contact_details = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    appartment_type = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    image=models.ImageField('images/',null=True)
    image1=models.ImageField('images/',null=True)
    image2=models.ImageField('images/',null=True)
    image3=models.ImageField('images/',null=True)
    image4=models.ImageField('images/',null=True)
    rent = models.CharField(max_length=50, null=True)
    rooms = models.CharField(max_length=50, null=True)
    bath_rooms = models.CharField(max_length=50, null=True)
    status= models.CharField(max_length=100,null=True)


class book_now(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    appartment = models.ForeignKey(add_appartment, on_delete=models.CASCADE, null=True)
    owner_id = models.ForeignKey(owner_reg, on_delete=models.CASCADE, null=True)
    time = models.TimeField(null=True)
    date= models.DateField(null=True)
    name = models.CharField(max_length=100,null=True)
    days = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    action= models.CharField(max_length=100,null=True)
    proof= models.FileField('file/',null=True)
    amount = models.CharField(max_length=100, null=True)
    payment = models.CharField(max_length=100, null=True)
    status2 = models.CharField(max_length=100, null=True)


class service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    appartment = models.ForeignKey(add_appartment, on_delete=models.CASCADE, null=True)
    services= models.CharField(max_length=100,null=True)
    service_status= models.CharField(max_length=100,null=True)
    status= models.CharField(max_length=100,null=True)



class payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    appartment = models.ForeignKey(add_appartment, on_delete=models.CASCADE, null=True)
    amount= models.CharField(max_length=100,null=True)
    payment=models.CharField(max_length=100,null=True)
    status= models.CharField(max_length=100,null=True)

class feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type= models.ForeignKey(UserType, on_delete=models.CASCADE, null=True)
    feedback = models.CharField(max_length=100,null=True)
    reply = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)








