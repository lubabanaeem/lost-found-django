from django.db import models

# Create your models here.

class Item(models.Model):
    TYPE_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]

    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Books', 'Books'),
        ('ID Card', 'ID Card'),
        ('Other', 'Other'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name