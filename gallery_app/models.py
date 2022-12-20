from django.core.exceptions import ValidationError
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


class AboutUs(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=2000)
    # if is_used == True => current description will be show in page
    is_used = models.BooleanField(default=False)

    def __str__(self):
        if self.is_used:
            return f'{self.title} is used'
        return f'{self.title} is not used'


class Address(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    phone = models.CharField(max_length=16)
    email = models.EmailField()

    # only one address could be created
    def clean(self):
        super().clean()
        if not self.id and Address.objects.exists():
            raise ValidationError('You cannot add more somethings.')
