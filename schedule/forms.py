from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name','phone_number','email','description','picture','category','owner')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Escreva Aqui'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Escreva Aqui'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Digite o número de telefone'}),
            'email': forms.TextInput(attrs={'placeholder': 'Digite o e-mail'}),
            'description': forms.Textarea(attrs={'placeholder': 'Conte mais...'}),
        }