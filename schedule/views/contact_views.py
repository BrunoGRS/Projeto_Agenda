from django.shortcuts import render, get_list_or_404, redirect
from schedule.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('id')
    
    paginator = Paginator(contacts, 15)  # Show 15 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    
    context = {
        'page_obj': page_obj,
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

def search(request):

    search_value = request.GET.get('q', '').strip()
    
    if search_value == "":
        return redirect('schedule:index')
    
    
    contacts = Contact.objects.filter(show=True).filter(Q(first_name__icontains=search_value) |
                                                        Q(last_name__icontains=search_value) |
                                                        Q(email__icontains=search_value) |
                                                        Q(phone_number__icontains=search_value)).order_by('id')
    
    paginator = Paginator(contacts, 15)  # Show 15 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos -',
    }
    return render(request, template_name='schedule/index.html', context=context)