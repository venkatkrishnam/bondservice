from django.db import models

# Create your models here.
class Bond(models.Model):
    cusip = models.CharField(max_length=9)
    issuer = models.CharField(max_length=20)
    currency = models.CharField(max_length=10)
    issueDate = models.DateField()
    maturityDate = models.DateField()
    coupon = models.DecimalField(max_digits=4, decimal_places=3)
    parValue = models.DecimalField(max_digits=12, decimal_places=6)
    paymentsPerYear = models.IntegerField(default=2)
    settleDelay = models.CharField(max_length=10, default='2D')
    description = models.CharField(max_length=100)
