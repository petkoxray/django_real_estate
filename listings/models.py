from autoslug import AutoSlugField
from django.db import models
from datetime import datetime
from realtors.models import Realtor


class ListingManager(models.Manager):
    def search(self, **kwargs):
        queryset_list = self.get_queryset().order_by('-list_date').filter(is_published=True)
        if kwargs['keywords']:
            queryset_list = queryset_list.filter(description__icontains=kwargs['keywords'])
        if kwargs['city']:
            queryset_list = queryset_list.filter(city__iexact=kwargs['city'])
        if kwargs['states']:
            queryset_list = queryset_list.filter(state__iexact=kwargs['states'])
        if kwargs['bedrooms']:
            queryset_list = queryset_list.filter(bedrooms__lte=kwargs['bedrooms'])
        if kwargs['prices']:
            queryset_list = queryset_list.filter(price__lte=kwargs['prices'])

        return queryset_list


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    objects = ListingManager()

    def __str__(self):
        return self.title
