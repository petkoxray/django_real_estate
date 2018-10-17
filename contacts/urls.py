from django.urls import path

from . import views

urlpatterns = [
    path('contact/<slug:listing_slug>', views.contact, name='contact')
]
