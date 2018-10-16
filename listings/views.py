from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

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

    return render(request, 'listings/listing.html', {
        'listing': listing
    })


def search(request):
    return render(request, 'listings/search.html')
