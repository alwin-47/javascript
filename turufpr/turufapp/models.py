from django.db import models

# Create your models here.
class Turufs(models.Model):
    Name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    des=models.CharField(max_length=150)
    def __str__(self):
        return self.Name
class Booking(models.Model):
    cname=models.CharField(max_length=100)
    cnum=models.CharField(max_length=100)
    Name=models.ForeignKey(Turufs,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
    
    