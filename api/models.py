from django.db import models

# Create your models here.

class Recommendedmodel(models.Model):
    id = models.CharField(primary_key=True,max_length=40)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    stars = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    location = models.CharField(max_length=40)
    updatedat = models.DateTimeField(auto_now=True)
    createdat = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updatedat', '-createdat']

    def __str__(self):
        return self.name


class Popularmodel(models.Model):
    id = models.CharField(primary_key=True,max_length=40)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    stars = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    location = models.CharField(max_length=40)
    updatedat = models.DateTimeField(auto_now=True)
    createdat = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updatedat', '-createdat']

    def __str__(self):
        return self.name


class usermodel(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    userid=models.CharField(primary_key=True,max_length=40)


class cartmodel(models.Model):
    productid=models.CharField(max_length=40)
    userid=models.CharField(max_length=40)
    count=models.IntegerField()


class favmodel(models.Model):
    productid=models.CharField(max_length=40)
    userid=models.CharField(max_length=40)
    isfav=models.CharField(max_length=5)
    