from django.forms import ModelForm

from contacts.models import Contact


class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['listing'].disabled = True

    class Meta:
        model = Contact
        fields = ['listing', 'phone', 'message']
