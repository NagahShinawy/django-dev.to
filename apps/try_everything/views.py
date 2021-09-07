from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django_tables2 import SingleTableView, Table
from import_export import resources
from .models import App
from .utils import from_resource_to_filename


class AppResource(resources.ModelResource):
    class Meta:
        from .models import App
        model = App


def home(request):
    apps = App.objects.all()
    return render(request, template_name="index.html", context={"apps_list": apps})


def to_excel(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=["POST"], status=405)
    app_resource = AppResource()
    fname = from_resource_to_filename(app_resource)
    response = HttpResponse(content_type="application/vnd.ms-excel")
    response['Content-Disposition'] = f'attachment; filename={fname}.xlsx'
    response.write(app_resource.export().xlsx)
    return response


class AppTable(Table):
    class Meta:
        model = App
        template_name = "index"
        fields = ("title", "created")
        attrs = {"class": "paleblue"}


class AppListView(SingleTableView):
    model = App
    template_name = 'index.html'
    table_class = AppTable