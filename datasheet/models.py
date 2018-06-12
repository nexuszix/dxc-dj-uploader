from django.db import models

# Create your models here.
class OrderCatalog(models.Model):
	code = models.CharField("Order Catalog Code", primary_key=True)
	long_desc = models.CharField("Long Description")
	short_desc = models.CharField("Short Description")
	order_cate = models.CharField("Order Category Code")
	order_type = models.CharField("Order Type Code")
	activity_type = models.CharField("Activity Type", default="", blank=True)
	status = models.BooleanField("Uploaded?", default=False)