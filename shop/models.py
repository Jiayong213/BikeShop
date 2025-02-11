from django.db import models

# Create your models here.
class Frame(models.Model):
    color = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color
    
class Seat(models.Model):
    color = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color
    
class Tire(models.Model):
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.type

class Basket(models.Model):
    quantity = models.IntegerField()

    def __str__(self):
        return self.quantity
    
class Bike(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description = models.TextField()
    has_basket = models.BooleanField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    CURRENT_STATUS = [
        ("pending", "P"),
        ("ready", "R"),
    ]
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=CURRENT_STATUS, default="pending")

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.phone_number