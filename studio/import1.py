import tablib
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from studio.models import contamination
class con_resource (resources.ModelResource):
    class Meta:
        model=contamination


con_resource =resources.modelresource_factory(model=contamination)()
dataset=tablib.dataset('experiment.csv',headers=False)
result=con_resource.import_data(dataset,dry_run=False) 