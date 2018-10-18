from django.core.exceptions import ValidationError
from django.forms import ModelForm

from contacts.models import Contact


class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields['listing'].disabled = True

    class Meta:
        model = Contact
        fields = ['listing', 'phone', 'message']

    def clean(self):
        cleaned_data = self.cleaned_data
        if Contact.objects.filter(user=self.user,
                                  listing=cleaned_data['listing']).exists():
            raise ValidationError(
                'Contact already exist')

        return cleaned_data
