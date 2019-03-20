from import_export import resources
from user.models import Reading

class Na_Reading(resources.ModelResource):

    class Meta:
        model = Reading
        # fields =('intensity', 'na_level')
