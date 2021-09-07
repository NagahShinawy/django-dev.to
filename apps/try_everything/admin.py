# https://django-import-export.readthedocs.io/en/stable/getting_started.html

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import CSV, XLS, XLSX
from import_export import resources
from .models import App


class AppResource(resources.ModelResource):
    class Meta:
        model = App


class AppImportExport(ImportExportModelAdmin):
    formats = (CSV, XLS, XLSX)  # export/import just these formats
    resource_class = AppResource


admin.site.register(App, AppImportExport)
