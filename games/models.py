from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q

import datetime as dt

Type=(
    ('Gamer','Gamer'),
    ('Developer','Developer'),
)

Payment=(
    ('Yes','Yes'),
    ('No','No'),
)

# Create your models here.
class countries(models.Model):
    countries= models.CharField(max_length=100)

    def __str__(self):
        return self.countries

class categories(models.Model):
    categories= models.CharField(max_length=100)

    def __str__(self):
        return self.categories

class platforms(models.Model):
    platforms = models.CharField(max_length=100)

    def __str__(self):
        return self.platforms

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = HTMLField()
    download = models.FileField(upload_to='downloads/')
    categories = models.ManyToManyField(categories)
    platforms = models.ManyToManyField(platforms)
    operating_system = models.CharField(max_length=100)
    CPU = models.CharField(max_length=100)
    RAM = models.CharField(max_length=100)
    HDDspace = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    screenshot1 = models.ImageField(upload_to='screenshots/')
    screenshot2 = models.ImageField(upload_to='screenshots/')
    screenshot3 = models.ImageField(upload_to='screenshots/')
    game_cover = models.ImageField(upload_to='gamecovers/')
    trailer = models.CharField(max_length=300)
    developer = models.ForeignKey(User,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    payment = models.CharField(max_length=15,choices=Payment,default='No')

    def __str__(self):
        return self.name


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    description = HTMLField()
    country = models.ForeignKey(countries,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname =models.CharField(max_length=100)
    lastname =models.CharField(max_length=100)
    email = models.EmailField()
    type = models.CharField(max_length=15,choices=Type,default='Gamer')

    def __str__(self):
        return self.firstname

class News(models.Model):
    news_pic = models.ImageField(upload_to='review_pictures/')
    title = models.CharField(max_length=100)
    news = HTMLField()
    post_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    review= models.ForeignKey(News,on_delete=models.CASCADE)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
