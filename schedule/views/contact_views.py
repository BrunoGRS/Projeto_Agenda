from django.shortcuts import render, get_list_or_404
from schedule.models import Contact
from django.http import Http404

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('id')
    
    context = {
        'contacts': contacts,
        'site_title': 'Contatos -',
    }
    return render(request, template_name='schedule/index.html', context=context)

def contact(request, contact_id):
    single_contact = Contact.objects.filter(pk=contact_id, show=True).first()
    
    if single_contact is None:
        raise Http404()
    
    single_title = f'{single_contact.first_name} {single_contact.last_name} - '
    
    context = {
        'contact': single_contact,
        'site_title': single_title,
    }
    return render(request, template_name='schedule/contact.html', context=context)
