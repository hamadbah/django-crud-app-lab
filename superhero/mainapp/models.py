from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Enemy(models.Model):
    name = models.CharField(max_length=100)
    attack_power = models.IntegerField()
    speed = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('enemies_detail', kwargs={'pk': self.id})
    
class Hero(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    image = models.ImageField(upload_to='mainapp/static/uploads', default='') # to upload image - you need to run library Pillow for image  pip install Pillow
    enemies = models.ManyToManyField(Enemy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # This shows the object name in Django admin instead of Object desc
    def __str__(self):
        return self.name
        # return f"{self.name}, {self.age}"
        
    def get_absolute_url(self):
        return reverse('detail', kwargs={'hero_id': self.id})
    
class Weapon(models.Model):
    name = models.CharField(max_length=100)
    power = models.IntegerField()
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)