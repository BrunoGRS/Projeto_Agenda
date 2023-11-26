from typing import Any
from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
import re
from schedule.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name','phone_number','email','description', 'picture', 'category')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Escreva Aqui'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Escreva Aqui'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Digite o número de telefone'}),
            'email': forms.TextInput(attrs={'placeholder': 'Digite o e-mail'}),
            'description': forms.Textarea(attrs={'placeholder': 'Conte mais...'})
        }
        
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if len(first_name) < 3:
            self.add_error('first_name',ValidationError('O nome deve possuir no mínimo 3 caracteres!', code= 'invalid'))
        
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
            
        if len(last_name) < 3:
            self.add_error('last_name',ValidationError('O nome deve possuir no mínimo 3 caracteres!', code= 'invalid'))

        return last_name
            
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        
        if not re.search(regex, email):
            self.add_error('email', ValidationError('Endereço de e-mail inválido', code='invalid'))
            
        return email
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error('email',ValidationError('Endereço de e-mail já cadastro', code='invalid'))
        else:
            return email