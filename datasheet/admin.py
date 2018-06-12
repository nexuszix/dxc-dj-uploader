from django.contrib import admin
from .models import OrderCatalog
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class OrderResource(resources.ModelResource):
	class Meta:
		model = OrderCatalog

@admin.register(OrderCatalog)
class OrderAdmin(ImportExportModelAdmin):
	resource_class = OrderResource
	list_display = ('code', 'long_desc', 'order_cate', 'order_type', 'activity_type', 'status',)
# # 	list_filter = ('province',)
	search_fields = ['code', 'long_desc']


admin.site.site_header = "DXC EM Datasheet Uploader"