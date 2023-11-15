from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from schedule.forms import ContactForm
from schedule.models import Contact


def create_contact(request):
    form_action = reverse('schedule:create')
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        
        context = {
            'form': form,
            'form_action': form_action
        }
        
        if form.is_valid():
            contact = form.save()
            return redirect('schedule:update', contact_id=contact.id)
            
        return render(request, template_name='schedule/create.html', context=context)
        
    context = {
        'form': ContactForm(),
        'form_action': form_action
        }
    
    return render(request, template_name='schedule/create.html', context=context)

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('schedule:update', args=(contact_id,))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        
        context = {
            'form': form,
            'form_action': form_action
        }
        
        if form.is_valid():
            contact = form.save()
            return redirect('schedule:update', contact_id=contact.id)
            
        return render(request, template_name='schedule/create.html', context=context)
        
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action
        }
    
    return render(request, template_name='schedule/create.html', context=context)

def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    
    confirmation = request.POST.get('confirmation', 'no')
    
    if confirmation == 'yes':
        contact.delete()
        return redirect('schedule:index')
    
    context = {
        'contact':contact, 
        'confirmation': confirmation
    }
    
    return render(request, template_name='schedule/contact.html', context=context)