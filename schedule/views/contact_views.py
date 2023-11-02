from django.shortcuts import render
from schedule.models import Contact

def index(request):
    contacts = Contact.objects.all()
    
    context = {
        'contacts': contacts,
    }
    return render(request, template_name='schedule/index.html', context=context)
