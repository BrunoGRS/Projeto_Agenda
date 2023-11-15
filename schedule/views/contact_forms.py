from django.shortcuts import render, redirect
from schedule.forms import ContactForm

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form
        }
        
        if form.is_valid():
            form.save()
            return redirect('schedule:create')
            
        return render(request, template_name='schedule/create.html', context=context)
        
    context = {
        'form': ContactForm()
        }
    
    return render(request, template_name='schedule/create.html', context=context)
