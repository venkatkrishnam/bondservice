from django.contrib import admin

from .models import Bond

# Register your models here.
class BondAdmin(admin.ModelAdmin):
	save_as = True
	list_display = ('cusip', 'issuer', 'currency', 'issueDate', 'maturityDate', 'parValue', 'coupon', 'paymentsPerYear', 'settleDelay', 'description')

admin.site.register(Bond, BondAdmin)