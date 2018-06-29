from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

#### Order Catalog #################
class OrderCatalogResource(resources.ModelResource):
	class Meta:
		model = OrderCatalog
		import_id_fields = ['code']

@admin.register(OrderCatalog)
class OrderCatalogAdmin(ImportExportModelAdmin):
	resource_class = OrderCatalogResource
	list_display = ('code', 'long_desc', 'order_type', 'activity_type', 'status',)
# # 	list_filter = ('province',)
	search_fields = ['code', 'long_desc', 'order_type__code', 'order_type__order_cate__code', 'status',]


#### Order Type #################
class OrderTypeResource(resources.ModelResource):
	class Meta:
		model = OrderType
		import_id_fields = ['code']

@admin.register(OrderType)
class OrderTypeAdmin(ImportExportModelAdmin):
	resource_class = OrderTypeResource
	list_display = ('code', 'desc', 'order_cate',)
# # 	list_filter = ('province',)
	search_fields = ['code', 'desc', 'order_cate__code']


#### Activity Type #################
class ActivityTypeResource(resources.ModelResource):
	class Meta:
		model = ActivityType
		import_id_fields = ['code']

@admin.register(ActivityType)
class ActivityTypeAdmin(ImportExportModelAdmin):
	resource_class = ActivityTypeResource
	list_display = ('code', 'desc', )
# # 	list_filter = ('province',)
	search_fields = ['code', 'desc', 'order_type__desc']


#### Order Category #################
class OrderCategoryResource(resources.ModelResource):
	class Meta:
		model = OrderCategory
		import_id_fields = ['code']
		
@admin.register(OrderCategory)

class OrderCategoryAdmin(ImportExportModelAdmin):
	resource_class = OrderCategoryResource
	list_display = ('code', 'desc', )
# # 	list_filter = ('province',)
	search_fields = ['code', 'desc']


admin.site.site_header = "DXC EM Datasheet Uploader"