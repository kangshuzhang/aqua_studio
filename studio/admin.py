from django.contrib import admin
from studio.models import contamination
from import_export import resources
from import_export.admin import ImportExportModelAdmin
admin.site.register(contamination)
class con_resource (resources.ModelResource):
    class Meta:
        model=contamination
class resourceadmin(ImportExportModelAdmin):
    resource_class= con_resource
# Register your models here.
