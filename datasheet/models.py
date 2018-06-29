from django.db import models

# Create your models here.
class OrderCategory(models.Model):
	code = models.CharField("Order Catagory Code", primary_key=True, max_length=20)
	desc = models.CharField("Order Category", max_length=60)

	def __str__(self):
		return self.code

class OrderType(models.Model):
	code = models.CharField("Order Type Code", primary_key=True, max_length=20)
	desc = models.CharField("Order Type", max_length=60)
	order_cate = models.ForeignKey(OrderCategory, on_delete=models.CASCADE)

	def __str__(self):
		return self.code

class ActivityType(models.Model):
	code = models.CharField("Activity Type Code", primary_key=True, max_length=20)
	desc = models.CharField("Activity Type", max_length=60)
	order_type = models.ForeignKey(OrderType, on_delete=models.CASCADE)

	def __str__(self):
		return self.code

class OrderCatalog(models.Model):
	code = models.CharField("Order Catalog Code", primary_key=True, max_length=20)
	long_desc = models.CharField("Long Description", max_length=60)
	short_desc = models.CharField("Short Description", max_length=40)
	order_type = models.ForeignKey(OrderType, on_delete=models.CASCADE)
	activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE, default="", blank=True)
	status = models.CharField("Status", default="New", max_length=100)

	def __str__(self):
		return self.code





