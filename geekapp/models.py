from django.db import models
from django.utils import timezone
import datetime

class Host(models.Model):

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

class Visitor(models.Model):

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    ischeckedin = models.BooleanField(default=False)
    checkin = models.TimeField(blank=True)
    checkout = models.TimeField(null=True, blank=True)

    def checkinrecord(self):
        self.checkin = str(str(timezone.now()).split('.')[0]).split(' ')[1]
        self.ischeckedin = True
        self.save()

    def checkoutrecord(self):
        self.checkout = str(str(timezone.now()).split('.')[0]).split(' ')[1]
        self.ischeckedin = False
        self.save()
