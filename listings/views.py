from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from contacts.forms import ContactForm
from listings.forms import SearchBox
from listings.models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    return render(request, 'listings/all_listings.html', {
        'listings': paged_listings
    })


def listing(request, listing_slug):
    listing = get_object_or_404(Listing, slug=listing_slug)
    form = ContactForm(user=request.user, initial={'listing': listing.id})

    return render(request, 'listings/listing.html', {
        'listing': listing,
        'form': form
    })


def search(request):
    form = SearchBox(request.GET, initial=request.GET)
    if form.is_valid():
        listings = Listing.objects.search(**form.cleaned_data)
    else:
        listings = Listing.objects.order_by('-list_date')

    return render(request, 'listings/search.html', {
        'form': form,
        'listings': listings
    })
