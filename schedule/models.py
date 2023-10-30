from django.db import models
from django.utils import timezone

class Category(models.Model):
    name_category = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f'{self.name_category}'
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture= models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'