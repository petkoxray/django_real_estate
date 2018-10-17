from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

from listings.models import Listing


class Contact(models.Model):
    listing = models.ForeignKey(Listing, null=False, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user.username
