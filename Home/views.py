# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the contact message to the database
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        return redirect('contact_success')  # Redirect to success page

    return render(request, 'contact.html')

def contact_success(request):
    return render(request, 'contact_success.html')
