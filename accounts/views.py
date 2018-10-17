from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from accounts.forms import UserRegisterForm
from contacts.models import Contact


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    return render(request, 'accounts/dashboard.html', {
        'contacts': user_contacts
    })
