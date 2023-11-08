from django.shortcuts import render
from schedule.forms import ContactForm

def create_contact(request):
    
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }
        
        return render(request, template_name='schedule/create.html', context=context)
        
    context = {
        'form': ContactForm()
        }
    
    return render(request, template_name='schedule/create.html', context=context)
