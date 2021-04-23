from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Driver(models.Model):
    # name=models.CharField(max_length=255)
    # email=models.EmailField(max_length=255)
    # phone=models.CharField(max_length=255)
    # LOCATION=(
    #     ('Kuniyamuthur','Kuniyamuthur'),
    #     ('Ukkadam','Ukkadam'),
    #     ('Gandhipuram','Gandhipuram'),
    #     ('Sundharapuram','Sundharapuram'),
    # )
    # Location=models.CharField(max_length=255,choices = LOCATION)
    # lic_no=models.IntegerField()
    # vehicle_no=models.CharField(max_length=255)
    # password=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    # user_id=models.CharField(max_length=10,null=True)
    # name=models.CharField(max_length=200,null=True)
    # email=models.EmailField(max_length=255,null=True)
    phone=models.CharField(max_length=255,null=True,blank=True)
    LOCATION=(
        ('Kuniyamuthur','Kuniyamuthur'),
        ('Ukkadam','Ukkadam'),
        ('Gandhipuram','Gandhipuram'),
        ('Sundharapuram','Sundharapuram'),
    )
    Location=models.CharField(max_length=255,choices = LOCATION,null=True)
    lic_no=models.IntegerField(null=True,blank=True)
    vehicle_no=models.CharField(max_length=255,null=True,blank=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)



    # def user(self):
    #     return User.objects.get(pk=self.user_id)

    def __str__(request):
        return str(request.user)


class Booking(models.Model):
    name=models.CharField(max_length=255,null=True)
    email=models.EmailField(max_length=255,null=True)
    phone=models.CharField(max_length=20,null=True)
    passenger=models.IntegerField(null=True)
    FROM_LOCATION=(
        ('Kuniyamuthur','Kuniyamuthur'),
        ('Ukkadam','Ukkadam'),
        ('Gandhipuram','Gandhipuram'),
        ('Sundharapuram','Sundharapuram'),
    )
    StartLocation=models.CharField(max_length=255,null=True,choices = FROM_LOCATION)
    TO_LOCATION=(
        ('Kuniyamuthur','Kuniyamuthur'),
        ('Ukkadam','Ukkadam'),
        ('Gandhipuram','Gandhipuram'),
        ('Sundharapuram','Sundharapuram'),
    )
    ToLocation=models.CharField(max_length=255,null=True,choices = TO_LOCATION)


    def __str__(self):
        return self.name
