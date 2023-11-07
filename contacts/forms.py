from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'notes']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')

        existing_contact_with_name = Contact.objects.filter(name=name).exclude(pk=self.instance.pk)
        existing_contact_with_email = Contact.objects.filter(email=email).exclude(pk=self.instance.pk)

        if existing_contact_with_name.exists():
            self.add_error('name', "A contact with this name already exists.")

        if existing_contact_with_email.exists():
            self.add_error('email', "A contact with this email already exists.")

