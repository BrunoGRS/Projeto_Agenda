from django.shortcuts import render, get_list_or_404, redirect
from schedule.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

def create_contact(request):
    search = request.POST.get('first_name')
    
    context = {
        'site_title': 'Criar -',
    }
    return render(request, template_name='schedule/create.html', context=context)