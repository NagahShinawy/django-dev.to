from django.urls import path
from .views import home, to_excel


urlpatterns = [
    path('', home, name="home"),
    path('export/', to_excel, name="to_excel"),
]
