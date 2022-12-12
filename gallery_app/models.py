from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images/', default='category_images/palette.jpg')

    def __str__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pictures/')
    description = models.TextField(max_length=500)
    date_created = models.DateField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
