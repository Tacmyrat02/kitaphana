from django.db import models


class Card(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    username = models.CharField(max_length=400)
    fakultet = models.CharField(max_length=400)
    kurs = models.CharField(max_length=300)
    profession = models.CharField(max_length=300)
    address = models.CharField(max_length=600)
    phoneNumber = models.CharField(max_length=30)
    birthDate = models.DateField(max_length=400)


class Book(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/%m')
    author = models.CharField(max_length=300)
    category = models.CharField(max_length=200)
    allNumber = models.IntegerField()
    pubDate = models.DateField()


class Record(models.Model):
    user = models.ForeignKey(
        Card, on_delete=models.CASCADE, related_name='recordsUser')
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='recordsBook')
    date = models.DateField(auto_now=True)

# Create your models here.
