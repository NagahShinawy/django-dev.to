from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from .views import home, to_excel
schema_view = get_swagger_view(title='Timeline API')


urlpatterns = [
    path('', home, name="home"),
    path('export/', to_excel, name="to_excel"),
    path('api/', schema_view, name="api"),
]
