from django.db import models

# Create your models here.


class Customer(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    mobile = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)


class Restaurant(models.Model):
    name = models.CharField(max_length = 20)
    picture = models.CharField(max_length = 20, default = "https://www.concretecms.com/application/files/9417/1778/2239/Restaurant_Websites.jpg")
    cuisine = models.CharField(max_length = 20)
    rating = models.FloatField(default = 0)

class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, related_name = "items")
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    price = models.FloatField()
    vegeterian = models.BooleanField(default=False)
    picture = models.URLField(max_length = 400, default='https://www.indiafilings.com/learn/wp-content/uploads/2024/08/How-to-Start-Food-Business.jpg')