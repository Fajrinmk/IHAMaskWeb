from django.db import models
from django.utils import timezone

# Create your models here.
class OrderList(models.Model):
    customerName = models.CharField(max_length=140, blank=False)
    customerEmail = models.EmailField(max_length=140, blank=False)
    customerPhone = models.CharField(max_length=140, blank=False)
    productQuantityA = models.IntegerField()
    productQuantityB = models.IntegerField()
    customerAddress = models.TextField(blank=False)
    productPrice = models.BigIntegerField() #Ini field baru zar
    shippingPrice = models.BigIntegerField() #Ini field baru zar
    grandTotalPrice = models.BigIntegerField(blank=False)
    promoCode = models.CharField(max_length=140, blank=True)
    paidFlage = models.BooleanField(default=False) #Ini field baru zar
    deliveredFlage = models.BooleanField(default=False) #Ini field baru zar
    created_on = models.DateTimeField(default=timezone.now)

class promoCode(models.Model):
	promoName = models.CharField(max_length=10, blank=False)
	promoAmount = models.FloatField(blank=False)

class upcomingEvents(models.Model):
	eventName= models.CharField(max_length=140, blank=False)
	eventURL= models.CharField(max_length=140, blank=False)
	eventDate= models.CharField(max_length=140, blank=False)
	eventVenue= models.CharField(max_length=140, blank=False)
	def __str__(self):
		return self.eventName

class FAQ(models.Model):
	titleIndo = models.TextField()
	titleEng = models.TextField()
	isiIndo = models.TextField()
	isiEng = models.TextField()
	def __str__(self):
		return self.titleEng
