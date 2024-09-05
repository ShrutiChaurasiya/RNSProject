from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Front(models.Model):
    bookname=models.TextField()
    book_desc=models.TextField()
    book_price=models.CharField(max_length=10)
    bookimage=models.ImageField(upload_to='images/',default='')
    
    def __str__(self):
        return "BookName:-"+self.bookname

class Product(models.Model):
    bookname=models.TextField()
    author_name=models.TextField()
    book_desc=models.TextField()
    book_price=models.CharField(max_length=10)
    bookimage=models.ImageField(upload_to='pimage/',default='')
    
    def __str__(self):
        return "BookName:-"+self.bookname

class Buy(models.Model):
    accountname=models.TextField()
    bname=models.TextField()
    cvv=models.CharField(max_length=5)
    Branch=models.TextField()
    Email=models.EmailField(max_length=254)

    def __str__(self):
        return "Account Name:-"+self.accountname

class Purchase(models.Model):
    name=models.TextField()
    email=models.EmailField(max_length=254)
    address=models.TextField()
    city=models.TextField()
    state=models.TextField()
    zip=models.TextField()
    cardName=models.TextField()
    cardNum=models.TextField()

    def __str__(self):
        return "Name:-"+self.name + self.email
