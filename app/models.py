from django.db import models

# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class SalesData(models.Model):
	ordernum = models.CharField(max_length=255, blank=False)
	sales_amount = models.IntegerField(null=False)
	cost_price = models.IntegerField(null=False)
	Trans_amount = models.IntegerField(null=False)
	Commission = models.IntegerField(null=False)
	Payment_charge =models.IntegerField(null=False)
	pickpack_fee = models.IntegerField(null=False)

class EasycomData(models.Model):
	ordernum = models.CharField(max_length=255, blank=False)
	profit_loss_per = models.IntegerField(null=False)
	Transferred_amount = models.IntegerField(null=False)
	Total_Mc = models.IntegerField(null=False)
