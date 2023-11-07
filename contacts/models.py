from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone  

class Contact(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    notes = models.TextField()
    created_time = models.DateTimeField(default=timezone.now, editable=False)

    def clean(self):
        existing_contact_with_name = Contact.objects.filter(name=self.name).exclude(pk=self.pk)
        existing_contact_with_email = Contact.objects.filter(email=self.email).exclude(pk=self.pk)

        if existing_contact_with_name.exists():
            raise ValidationError("A contact with this name already exists.")

        if existing_contact_with_email.exists():
            raise ValidationError("A contact with this email already exists.")
