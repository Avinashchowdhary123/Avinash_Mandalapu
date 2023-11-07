from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})
