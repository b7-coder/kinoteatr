from django.db import models
from django.conf import settings

class Products(models.Model):
    image = models.ImageField() # новая строка
    name = models.CharField(max_length=100)
    description = models.TextField()
    types = [
        ('TVS','TV Series'),
        ('Пол.метр.','Полнометражный' ),
        ('Кор.метр.','Короткометражный'),
    ]
    type = models.CharField(max_length=50,choices=types)
    studios = models.CharField(max_length=255)
    statuses = [
        ('Зак.','Законнченный'),
        ('В раз','В разработке')
    ]
    status = models.CharField(max_length=100)
    duration = models.FloatField()
    qualities = [
        ('HD','HD'),
        ('FHD','FHD'),
        ('LOW','LOW',),
        ('2k','2K')
    ]
    quality = models.CharField(max_length=100,choices=qualities)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class ProductsImages(models.Model):
  productObject = models.ForeignKey(Products, on_delete=models.CASCADE)
  image = models.ImageField()
  created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
	userObject = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
	productObject = models.ForeignKey(Products,on_delete=models.CASCADE)
	score = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

# products-serias

class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

class ProductsCategories(models.Model):
    productObject = models.ForeignKey(Products, on_delete=models.CASCADE)
    categoryObject = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Comments(models.Model):
    productObject = models.ForeignKey(Products, on_delete=models.CASCADE)
    userObject = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class News(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class NewsDetails(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField()
    newsObject = models.ForeignKey(News, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class OurBlog(models.Model):
    # PO - product object foreign key
    leftBigImagePO = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='big1') 
    rightBigImagePO = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='big2')
    firstTopSmallImagePO = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='small1')
    secondTopSmallImagePO = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='small2')
    firstLowSmallImagePO = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='small3')
    secondLowSmallImagePO = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='small4')