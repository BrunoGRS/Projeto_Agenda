from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from schedule.forms import RegisterForm
from django.contrib import messages


def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso')
            
            context = {
            'form': form
            }

            return redirect('schedule:index')
        else:
            print('deu errado')
    context = {
            'form': form
        }
    
    return render(request, 'schedule/register.html', context=context)