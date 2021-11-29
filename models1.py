from django.db import models


class order(models.Model):
    billing_number = models.BigIntegerField(primary_key=True)
    customer= models.CharField(max_length=100)
    price = models.IntegerField()
    purchase_date =models.dateTimeField()
    company= models.CharField(max_length=100)
    serial_number = models.BigIntegerField()
    mfg_date = models.DateTimeField()