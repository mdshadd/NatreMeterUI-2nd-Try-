from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Reading
from .models import sign


# Register your models here.

admin.site.register(sign)


@admin.register(Reading)
class ReadAdmin(ImportExportModelAdmin):
    pass
