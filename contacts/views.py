from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from contacts.forms import ContactForm
from contacts.models import Contact
from listings.models import Listing


@login_required
def contact(request, listing_slug):
    if request.method == 'POST':
        listing = get_object_or_404(Listing, slug=listing_slug)
        contact = Contact(user=request.user, listing=listing)
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
            return redirect('listing', listing_slug)
        else:
            return render(request, 'listings/listing.html', {
                'listing': listing,
                'form': form
            })
