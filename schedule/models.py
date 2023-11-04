from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    name_category = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f'{self.name_category}'
    
class Contact(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        
    first_name = models.CharField(max_length=50, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=50, verbose_name='último Nome')
    phone_number = models.CharField(max_length=15, verbose_name='Telefone')
    email = models.EmailField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Data de Criação')
    description = models.TextField(blank=True, verbose_name='Descrição')
    show = models.BooleanField(default=True, verbose_name='Mostrar')
    picture= models.ImageField(blank=True, upload_to='pictures/%Y/%m', verbose_name='Foto')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Categoria')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Criado por:')
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'