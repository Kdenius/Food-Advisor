# models.py
from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone

class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=100,unique=True)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_no = models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Advisor(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    specification = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Item(models.Model):
    CATEGORY_CHOICES = (
        ('F','fruit'),
        ('V','vegetable'),
        ('J','junk food'),
        ('D', 'dairy product'),
        ('S', 'sweets'),
        ('C', 'cold drink'),
    )
    item_name = models.CharField(max_length=100)
    VITAMIN_CHOICES = (
        ('A', 'A'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('K', 'K'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
        ('B6', 'B6'),
        ('B12', 'B12'),
        ('B5', 'B5'),
        ('B7', 'B7'),
        ('B9', 'B9'),
    )
    vitamin = MultiSelectField(max_length=100,choices=VITAMIN_CHOICES,null=True,blank=True)
    category = models.CharField(max_length=1,choices=CATEGORY_CHOICES)
    calories = models.IntegerField()
    ingredient = models.CharField(max_length=100)
    image = models.ImageField()
    def __str__(self):
        return self.item_name

class Report(models.Model):
    pr_nm = models.ForeignKey(Person,on_delete=models.CASCADE,default=1)
    date = models.DateField(default=timezone.now)
    total_calories = models.IntegerField()
    total_vitamins = models.CharField(max_length=200)
    consumed_items = models.CharField(max_length=200)
    total_ingredient = models.CharField(max_length=200)

class Favorite_list(models.Model):
    pr_name = models.ForeignKey(Person,on_delete=models.CASCADE,default=1)
    item_id = models.ForeignKey(Item,on_delete=models.CASCADE)

class Eaten(models.Model):
    pr_name = models.ForeignKey(Person,on_delete=models.CASCADE,default=1)
    item_id = models.ForeignKey(Item,on_delete=models.CASCADE)
    date = models.DateField(default='2024-2-12')
    quntity = models.IntegerField()


class Target(models.Model):
    pr_nm = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)
    tr_calories = models.IntegerField()
    VITAMIN_CHOICES = (
        ('A', 'A'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('K', 'K'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
        ('B6', 'B6'),
        ('B12', 'B12'),
        ('B5', 'B5'),
        ('B7', 'B7'),
        ('B9', 'B9'),
    )
    tr_vitamins = MultiSelectField(max_length=100,choices=VITAMIN_CHOICES,null=True, blank=True, default=1)
    # tr_ingredient = models.CharField(max_length=100)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
class Advice(models.Model):
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    description = models.TextField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    
